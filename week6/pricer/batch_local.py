import json
import pickle
import time
import logging
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import ollama

MODEL = "llama3.2:latest"
BATCHES_FOLDER = "batches"
OUTPUT_FOLDER = "output"
state = Path("batches.pkl")

SYSTEM_PROMPT = """Create a concise product description. You MUST strictly follow the format. Any deviation is incorrect. Do not include part numbers.

Follow EXACT format (no exceptions):
Title: Rewritten short precise title
Category: eg Electronics
Brand: Brand name
Description: 1 sentence description
Details: 1 sentence on features

Rules:
- Output ONLY these 5 lines in this exact order
- Do NOT add extra lines, text, punctuation, or explanations
- Do NOT rename, reorder, or modify fields
- Do NOT include part/model numbers
- Each field must be minimal and precise"""


class Batch:
    BATCH_SIZE = 1000
    batches = []
    # Number of parallel worker threads for per-batch inference. Set to 1 for sequential.
    WORKERS = 4
    # Per-call retry attempts for transient failures
    RETRIES = 2
    # Backoff base seconds
    BACKOFF = 0.5

    def __init__(self, items, start, end, lite):
        self.items = items
        self.start = start
        self.end = end
        self.done = False

        self.filename = f"{start}_{end}.jsonl"

        folder = Path("lite") if lite else Path("full")
        # avoid shadowing the class-level `batches` list
        self.batches_dir = folder / BATCHES_FOLDER
        self.output = folder / OUTPUT_FOLDER

        self.batches_dir.mkdir(parents=True, exist_ok=True)
        self.output.mkdir(parents=True, exist_ok=True)

    # -----------------------------
    # Prompt builder
    # -----------------------------
    def make_prompt(self, item):
        return [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": item.full},
        ]

    # -----------------------------
    # Local inference (replacement for Groq batch API)
    # -----------------------------
    def run_inference(self, messages):
        # resilient call with simple retries and exponential backoff
        last_exc = None
        for attempt in range(self.RETRIES + 1):
            try:
                response = ollama.chat(model=MODEL, messages=messages)
                return response["message"]["content"]
            except Exception as e:
                last_exc = e
                wait = self.BACKOFF * (2 ** attempt)
                logging.warning(f"ollama.chat failed (attempt {attempt+1}): {e}; retrying in {wait:.2f}s")
                time.sleep(wait)

        # final raise if all retries failed
        raise last_exc

    # -----------------------------
    # Process a single item
    # -----------------------------
    def process_item(self, item):
        messages = self.make_prompt(item)
        return self.run_inference(messages)

    # -----------------------------
    # Save intermediate JSONL (optional, for logging/debug)
    # -----------------------------
    def make_file(self):
        batch_file = self.batches_dir / self.filename

        with batch_file.open("w") as f:
            for item in self.items[self.start:self.end]:
                record = {
                    "id": item.id,
                    "input": item.full
                }
                f.write(json.dumps(record) + "\n")

    # -----------------------------
    # Main execution (replaces send/submit/fetch pipeline)
    # -----------------------------
    def execute(self):
        batch_output_file = self.output / self.filename

        results = []

        # timing
        start_time = time.time()

        slice_items = list(self.items[self.start:self.end])

        if self.WORKERS and self.WORKERS > 1:
            # parallel execution
            with ThreadPoolExecutor(max_workers=self.WORKERS) as exe:
                future_to_item = {exe.submit(self.process_item, item): item for item in slice_items}

                for future in tqdm(as_completed(future_to_item), total=len(future_to_item)):
                    item = future_to_item[future]
                    try:
                        summary = future.result()
                        item.summary = summary
                        results.append({"custom_id": item.id, "response": summary})
                    except Exception as e:
                        logging.exception("Error processing item %s", item)
                        results.append({"custom_id": item.id, "error": str(e)})
        else:
            # sequential fallback
            for item in tqdm(slice_items):
                try:
                    summary = self.process_item(item)
                    item.summary = summary
                    results.append({"custom_id": item.id, "response": summary})
                except Exception as e:
                    logging.exception("Error processing item %s", item)
                    results.append({"custom_id": item.id, "error": str(e)})

        # Save results
        with batch_output_file.open("w") as f:
            for r in results:
                f.write(json.dumps(r) + "\n")

        elapsed = time.time() - start_time
        logging.info(f"Batch {self.filename} processed {len(slice_items)} items in {elapsed:.2f}s")

        self.done = True

    # -----------------------------
    # CLASS METHODS (unchanged interface)
    # -----------------------------
    @classmethod
    def create(cls, items, lite):
        # reset any previously-created batches to avoid duplicates
        cls.batches = []

        for start in range(0, len(items), cls.BATCH_SIZE):
            end = min(start + cls.BATCH_SIZE, len(items))
            batch = Batch(items, start, end, lite)
            cls.batches.append(batch)

        print(f"Created {len(cls.batches)} batches")

    @classmethod
    def run(cls):
        for batch in tqdm(cls.batches):
            batch.make_file()
            batch.execute()

        print(f"Executed {len(cls.batches)} batches")

    @classmethod
    def fetch(cls):
        finished = [b for b in cls.batches if b.done]
        print(f"Finished {len(finished)} of {len(cls.batches)} batches")

        # apply outputs
        for batch in cls.batches:
            if not batch.done:
                continue

            output_file = batch.output / batch.filename

            if not output_file.exists():
                continue

            with open(output_file, "r") as f:
                for line in f:
                    data = json.loads(line)

                    item_id = data["custom_id"]
                    summary = data.get("response", "")

                    # `custom_id` may not be a list index; find the matching item by id
                    matched = next((it for it in batch.items if it.id == item_id), None)
                    if matched is not None:
                        matched.summary = summary

    @classmethod
    def save(cls):
        items = cls.batches[0].items if cls.batches else None

        for b in cls.batches:
            b.items = None

        with state.open("wb") as f:
            pickle.dump(cls.batches, f)

        for b in cls.batches:
            b.items = items

        print(f"Saved {len(cls.batches)} batches")

    @classmethod
    def load(cls, items):
        with state.open("rb") as f:
            cls.batches = pickle.load(f)

        for b in cls.batches:
            b.items = items

        print(f"Loaded {len(cls.batches)} batches")