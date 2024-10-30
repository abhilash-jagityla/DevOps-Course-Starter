import pymongo
import dotenv
import os

dotenv.load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGODB_CONNECTION_STRING"))

db = client[os.getenv("MONGODB_DATABASE_NAME")]

collection = db[os.getenv("MONGODB_COLLECTION_NAME")]

# Insert  a record
collection.insert_one({"description": "A second pymongo document"})

# Read a record
list (collection.find())

# Insert and update a record
collection.insert_one({"description": "An updateable document", "type": "updateable"})
collection.update_one({"type": "updateable"}, {"$set" : {"description": "CHANGED!!!"}})


print(collection)