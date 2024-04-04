from enum import Enum

class EnumChatSessionState(Enum):
  PREV_CONVERSATION = "previous_conversations"
  ACTUAL_CONVERSATION = "actual_conversation"
  CURRENT_CONVERSATION_SAVED = "current_conversation_saved"
  SELECTED_MODEL = "selected_model"