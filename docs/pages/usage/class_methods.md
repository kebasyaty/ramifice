Examples of frequently used methods:

```py title="main.py" linenums="1"
# Gets an estimate of the count of documents in a collection using collection metadata.
count: int = await User.estimated_document_count()

# Gets an estimate of the count of documents in a collection using collection metadata.
q_filter = {"first_name": "John"}
count: int = await User.count_documents(q_filter)

# Runs an aggregation framework pipeline.
from bson.bson import BSON
pipeline = [
    {"$unwind": "$tags"},
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
    {"$sort": BSON([("count", -1), ("_id", -1)])},
]
docs = await User.aggregate(pipeline)

# Finds the distinct values for a specified field across a single collection.
q_filter = "key_name"
values = await User.distinct(q_filter)

# Get collection name.
name = await User.collection_name()

# The full name is of the form database_name.collection_name.
name = await User.collection_full_name()

# Get AsyncBatabase for the current Model.
database = await User.database()

# Get AsyncCollection for the current Model.
collection = await User.collection()

# Find a single document.
q_filter = {"email": "John_Smith@gmail.com"}
mongo_doc = await User.find_one(q_filter)

# Create object instance from Mongo document.
q_filter = {"email": "John_Smith@gmail.com"}
mongo_doc = await User.find_one(q_filter)
user = User.from_mongo_doc(mongo_doc)

# Find a single document and converting to raw document.
q_filter = {"email": "John_Smith@gmail.com"}
raw_doc = await User.find_one_to_raw_doc(q_filter)

# Find a single document and convert it to a Model instance.
q_filter = {"email": "John_Smith@gmail.com"}
user = await User.find_one_to_instance(q_filter)

# Find a single document and convert it to a JSON string.
q_filter = {"email": "John_Smith@gmail.com"}
json = await User.find_one_to_json(q_filter)

# Find a single document and delete it.
q_filter = {"email": "John_Smith@gmail.com"}
delete_result = await User.delete_one(q_filter)

# Find a single document and delete it, return original.
q_filter = {"email": "John_Smith@gmail.com"}
mongo_doc = await User.find_one_and_delete(q_filter)

# Find documents.
q_filter = {"first_name": "John"}
mongo_docs = await User.find_many(q_filter)

# Find documents and convert to a raw documents.
q_filter = {"first_name": "John"}
raw_docs = await User.find_many_to_raw_docs(q_filter)

# Find documents and convert to a json string.
q_filter = {"email": "John_Smith@gmail.com"}
json = await User.find_many_to_json(q_filter)

# Find documents matching with Model.
q_filter = {"email": "John_Smith@gmail.com"}
delete_result = await User.delete_many(q_filter)

# Creates an index on this collection.
from pymongo import ASCENDING
keys = [("email", ASCENDING)]
result: str = await User.create_index(keys, name="idx_email")

# Drops the specified index on this collection.
User.drop_index("idx_email")

# Create one or more indexes on this collection.
from pymongo import ASCENDING, DESCENDING
index_1 = IndexModel([("username", DESCENDING), ("email", ASCENDING)], name="idx_username_email")
index_2 = IndexModel([("first_name", DESCENDING)], name="idx_first_name")
result: list[str] = await User.create_indexes([index_1, index_2])

# Drops all indexes on this collection.
User.drop_index()

# Get information on this collection’s indexes.
result = await User.index_information()

# Get a cursor over the index documents for this collection.
async for index in await User.list_indexes():
    print(index)

# Units Management.
# Management for `choices` parameter in dynamic field types.
# Units are stored in a separate collection.
from ramifice import Unit
unit = Unit(
  field="field_name",  # The name of the dynamic field.
  title={"en": "Title", "ru": "Заголовок"},  # The name of the choice item.
  value="Some text ...",  # The value of the choice item.
                          # Hint: float | int | str
  is_delete=False, # True - if you need to remove the item of choice.
                   # by default = False (add item to choice)
)
await User.unit_manager(unit)
```
