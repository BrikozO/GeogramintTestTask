import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

client = pymongo.MongoClient(os.getenv('MONGODB_HOST'), int(os.getenv('MONGODB_PORT')))

db = client[os.getenv('MONGO_INITDB_DATABASE')]
results_info_collection = db[os.getenv('MONGODB_RESULTS_COLLECTION')]
users_collection = db[os.getenv('MONGODB_USERS_COLLECTION')]
groups_collection = db[os.getenv('MONGODB_GROUPS_COLLECTION')]
