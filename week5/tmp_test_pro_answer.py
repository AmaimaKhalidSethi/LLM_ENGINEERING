import sys
from pathlib import Path
import traceback

# ensure repo root on path
sys.path.append(str(Path(__file__).resolve().parent.parent))

try:
    from week5.pro_implementation import answer as pro_answer
    print('Imported pro_implementation.answer')
    print('DB path:', pro_answer.DB_NAME)
    print('Collection name:', pro_answer.collection.name)
    print('Collection count:', pro_answer.collection.count())
    chunks = pro_answer.fetch_context_unranked('Who won the IIOTY award?')
    print('Retrieved', len(chunks), 'chunks')
    for i, c in enumerate(chunks[:3]):
        print(i, repr(c.page_content[:200]))
except Exception as e:
    print('Exception:')
    traceback.print_exc()
