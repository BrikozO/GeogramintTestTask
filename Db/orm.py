from datetime import datetime
from typing import Mapping, Any

from bson import ObjectId
from pymongo.collection import Collection
from pymongo.results import InsertOneResult, InsertManyResult

from Db import results_info_collection


class CollectionDocsInserter:

    def __init__(self, collection: Collection[Mapping[str, Any]]):
        self.collection = collection

    def insert_docs_and_get_ids(self, objects):
        result: InsertManyResult = self.collection.insert_many(objects)
        return result.inserted_ids


def insert_scanning_results_object(users_ids: list[ObjectId], groups_ids: list[ObjectId]) -> InsertOneResult:
    scanning_results_dict: dict = {
        'date': datetime.now(),
        'users': users_ids,
        'groups': groups_ids,
    }
    return results_info_collection.insert_one(scanning_results_dict)
