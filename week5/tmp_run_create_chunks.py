import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from week5.pro_implementation import ingest as ingest_mod

print('Loaded documents count:')
docs = ingest_mod.fetch_documents()
print(len(docs))
chunks = ingest_mod.create_chunks(docs)
print('Chunks created:', len(chunks))
print('Sample chunk:', chunks[0].page_content[:200])
