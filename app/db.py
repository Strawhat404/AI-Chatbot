from pymongo import MongoClient
from app.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.chatbot_db
collection = db.conversations

def save_conversation(user_id,conversation):
    collection.insert_one({"user_id":user_id, "conversation":conversation})