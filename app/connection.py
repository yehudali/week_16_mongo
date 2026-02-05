from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()


def get_db_collection():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://mongodb-gerstnir-dev.apps.rm2.thpm.p1.openshiftapps.com:27017/")
    mongo_db = os.getenv("MONGO_DB", "testdb")
    mongo_collection = os.getenv("MONGO_COLLECTION", "testcollection")
    client = MongoClient(mongo_uri)
    db = client[mongo_db]
    Collection = db[mongo_collection]
    return Collection


def close_connection(Collection):
        Collection.close()
        print("MongoDB connection closed")
