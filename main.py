from tinydb import TinyDB
from tinydb.database import Document


db = TinyDB('db.json', indent=4)

# document = Document(
#     {"first_name": "Javohir", "last_name": "Jalilov"},
#     doc_id=10
#     )


print(db.get(doc_id=11))