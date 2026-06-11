import importlib.util
import sys
import types
from pathlib import Path

# Inject a mock `ollama` module so importing batch_local doesn't fail in tests
mock_ollama = types.ModuleType("ollama")
def _mock_chat(model, messages):
    return {"message": {"content": "MOCK_RESPONSE"}}
mock_ollama.chat = _mock_chat
sys.modules["ollama"] = mock_ollama

# Load batch_local.py directly to avoid package import issues in test environment
mod_path = Path(r"C:/Users/HP/Desktop/LLM_ENGINEERING/week6/pricer/batch_local.py")
spec = importlib.util.spec_from_file_location("batch_local", str(mod_path))
batch_local = importlib.util.module_from_spec(spec)
spec.loader.exec_module(batch_local)
Batch = batch_local.Batch

# Simple dummy Item for testing
class DummyItem:
    def __init__(self, id, full):
        self.id = id
        self.full = full
        self.summary = None

    def __repr__(self):
        return f"DummyItem(id={self.id})"

# Mock run_inference to avoid calling ollama during the smoke test
def mock_run_inference(self, messages):
    # return a deterministic summary that includes batch range
    return f"MOCK_SUMMARY_{self.start}_{self.end}"

Batch.run_inference = mock_run_inference

# Create a small list of items
items = [DummyItem(i, f"full text {i}") for i in range(10)]

# Create batches, run, fetch
Batch.create(items, lite=True)
Batch.run()
Batch.fetch()

# Print results and check
for i, it in enumerate(items):
    print(i, it.summary)

missing = [i for i, it in enumerate(items) if not it.summary]
print("missing:", missing)
if missing:
    raise SystemExit(1)

print("SMOKE TEST PASSED")
