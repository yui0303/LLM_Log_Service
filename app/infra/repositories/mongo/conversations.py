from pymongo import MongoClient
from bson import ObjectId

from app.core.entity.conversation import Conversation

class MongoConversationsRepository:
    def __init__(self, mongo_uri: str, db_name: str, collection_name: str):
        # 初始化 MongoDB 客戶端和 collection
        self.client = MongoClient(mongo_uri)
        self.collection = self.client[db_name][collection_name]

    def create_conversation(self) -> str:
        # 建立新的對話並回傳對話的 id
        conversation = {
            "history": []
        }
        result = self.collection.insert_one(conversation)
        return str(result.inserted_id)

    def append_conversation(self, conversation_id: str, message: Conversation) -> bool:
        # 將新的對話紀錄新增至指定的對話 id 中
        conversation_obj = message.to_dict()
        result = self.collection.update_one(
            {"_id": ObjectId(conversation_id)},
            {"$push": {"history": conversation_obj}}
        )

        if result.matched_count > 0:
            if result.modified_count > 0:
                return True
        return False