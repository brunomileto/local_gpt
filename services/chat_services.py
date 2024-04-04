from calendar import c
import streamlit as st
from openai import OpenAI
from typing import List
from enums.EnumChatRoles import EnumChatRoles
from enums.EnumModels import EnumModels
from models.ChatMessage import ChatMessage
from services.chat_session_state_service import ChatSessionStateService


class ChatService:

  def __init__(self, api_key:str, chat_state: ChatSessionStateService) -> None:
    self.client = OpenAI(api_key=api_key)
    self.chat_state = chat_state
    self.selected_model = self.select_model()
  
  def select_model(self) -> None:
      selected_model = st.selectbox("Escolha um modelo", [""] + list(EnumModels.all_descriptions()))
      if selected_model:
        self.chat_state.selected_model = EnumModels.get_model_by_description(selected_model)
  
  #TODO: I'M TRYING TO FIX THIS METHOD.
  # SO 'ATUAL' HAS NO CONVERSATION ASSOCIATED
  # MY IDEA IS TO NOT USE 'ATUAL'. INSTEAD USE THE LIST OF PREV CONVERSATION
  # WHERE THE PREV CONVERSATION WILL HAVE ALSO, THE ACTUAL CONVERSATION ALWAYS
  # THE INDEX WILL BE THE 'KEY' TO KNOW IN WHICH CONVERSATION I'M
  # MAYBE CONVERT PREV CONVERSATION INTO A DICT?
  # WHEN STARTING A NEW CONVERSATION OR WHEN LOAD ANOTHER CONVERSATION
  # THIS METHOD SHOULD CONSIDER THAT.
  def render_sidebar_controls(self):
    new_convo_button = st.button("Inicie uma nova conversa")
    
    if new_convo_button:
      self.chat_state.start_new_conversation()
    conversations = [f"Conversa {key}" for key in sorted(self.chat_state.conversations.keys())]
    prev_convo_list = st.radio("Conversas", conversations)
    conversation_key = int(prev_convo_list.split(" ")[-1])
    if conversation_key != self.chat_state.actual_conversation_key:
      self.load_conversation(int(prev_convo_list.split(" ")[-1]))
    
  def load_conversation(self, conversation_index):
    self.chat_state.load_specific_conversation(conversation_index)
    
  def render_conversation(self):  
    for msg in self.chat_state.conversations[self.chat_state.actual_conversation_key]:
      st.chat_message(msg.role).write(msg.content)
      self.validate_model()
  
  def get_user_input(self):
    return st.chat_input()

  def validate_model(self) -> None:
    if not self.chat_state.selected_model:
      st.info("Primeiro selecione um modelo")
      st.stop()
    
  def process_user_input(self, user_input):
    self.validate_model()
    user_message = ChatMessage(role=EnumChatRoles.USER, content=user_input)
    st.chat_message(user_message.role).write(user_message.content)
    self.chat_state.update_conversation(user_message)
    self.generate_response(user_message.content)
  
  def generate_response(self, prompt:str):
    response = self.client.chat.completions.create(model=self.chat_state.selected_model.model_name, 
                                                   messages=self.chat_state.actual_conversation_json_list())
    ai_message_response = ChatMessage(role=EnumChatRoles.ASSISTANT, content=response.choices[0].message.content)
    self.chat_state.update_conversation(ai_message_response)
    self.render_message(ai_message_response)
  
  def render_message(self, chat_message:ChatMessage):
    st.chat_message(chat_message.role).write(chat_message.content)