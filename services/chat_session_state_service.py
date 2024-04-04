from typing import Dict, List
from enums.EnumModels import EnumModels
from models.ChatMessage import ChatMessage
from services.session_state_service import SessionStateService

class ChatSessionStateService:
    SELECTED_MODEL_KEY:str = "chat_selected_model"
    ACTUAL_CONVERSATION_KEY:str = "chat_actual_conversation_key"
    CONVERSATIONS:str = "chat_conversations"

    def __init__(self, session_state_service: SessionStateService, default_chat_message: ChatMessage) -> None:
        self.state_service = session_state_service
        self.default_chat = default_chat_message
    
    @property
    def conversations(self) -> Dict[int, List[ChatMessage]]:
        conversations = self.state_service.get(self.CONVERSATIONS)
        if not conversations:
            conversations = {1: [self.default_chat]}
            self.state_service.set(self.CONVERSATIONS, conversations)
        return conversations

    @property
    def selected_model(self) -> EnumModels | None:
        selected_model = self.state_service.get(self.SELECTED_MODEL_KEY)
        return selected_model

    @property
    def actual_conversation_key(self) -> int:
        actual_key = self.state_service.get(self.ACTUAL_CONVERSATION_KEY)
        if not actual_key:
            actual_key = 1
        return actual_key
    
    @selected_model.setter
    def selected_model(self, value:EnumModels) -> None:
        if not isinstance(value, EnumModels):
            raise ValueError("Selected model must be EnumModels")
        self.state_service.set(self.SELECTED_MODEL_KEY, value)

    def load_specific_conversation(self, conversation_key:int):
        self.state_service.set(self.ACTUAL_CONVERSATION_KEY, conversation_key)
        
    def start_new_conversation(self) -> None:
        conversations = self.conversations
        for key in sorted(conversations.keys(), reverse=True):
            conversations[key + 1] = conversations.pop(key)
        conversations[1] = [self.default_chat]       
        self.state_service.set(self.CONVERSATIONS, conversations)    
        self.state_service.set(self.ACTUAL_CONVERSATION_KEY, 1)
            
    def update_conversation(self, value: ChatMessage):  
        if not isinstance(value, ChatMessage):
            raise ValueError("Actual conversation must be a ChatMerssage")
        conversations = self.conversations
        actual_conversation = conversations[self.actual_conversation_key]
        actual_conversation.append(value)
        conversations[self.actual_conversation_key] = actual_conversation
        self.state_service.set(self.CONVERSATIONS, conversations)
    
    def actual_conversation_json_list(self) -> List[dict]:
        messages = [msg.to_dict() for msg in self.conversations[self.actual_conversation_key]]
        print(messages)
        return messages