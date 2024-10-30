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
    items = []
    return items
    pass
def move_item_to_done():
    pass
