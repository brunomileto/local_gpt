import redis
import json
from typing import List

from models.ChatMessage import ChatMessage

class RedisInterface:
    def __init__(self, host='localhost', port=6379, db=0):
      self.client = redis.Redis(host=host, port=port, db=db)
    
    def save_chat_message(self, chat_messages: List[ChatMessage], session_id:str):
      messages_data = [msg.to_dict() for msg in chat_messages]
      key = f"chat_history:{session_id}_{chat_messages[1].content[:10]}"
      
