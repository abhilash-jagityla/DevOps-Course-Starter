import pymongo
import os

client = pymongo.MongoClient(os.getenv("MONGODB_CONNECTION_STRING"))

db = client[os.getenv("MONGODB_DATABASE_NAME")]

collection = db[os.getenv("MONGODB_COLLECTION_NAME")]


def add_item(new_todo_title: str):
    new_items = {
        "name": new_todo_title,
        "status": "TO DO"
    }

    collection.insert_one(new_items)
def get_items(): 
    mongodb_documents = list(collection.find())

    items = []
    return items

    for document in mongodb_documents:
        items = Item.from_mongo_document(document)
        items.append(item)   

    return items

def move_item_to_done(todo_id: str):
    collection.update_one({"_id": objectId(todo_id)}, {"$set" : {"status": "Done"}})
    pass
