import streamlit as st

from enums.EnumChatRoles import EnumChatRoles
from models.ChatMessage import ChatMessage
from services.chat_services import ChatService
import dotenv
import os

from services.chat_session_state_service import ChatSessionStateService
from services.session_state_service import SessionStateService

dotenv.load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
session_state_service = SessionStateService()
chat_message = ChatMessage(role=EnumChatRoles.ASSISTANT, content="Como posso te ajudar?")
chat_session_state_service = ChatSessionStateService(session_state_service, chat_message)
chat_service = ChatService(openai_api_key, chat_session_state_service)

st.title("💬 Chat")
st.caption("🚀 Chatbot Simples!")

with st.sidebar:
    st.header("Conversas")
    chat_service.render_sidebar_controls()

chat_service.render_conversation()

user_input = chat_service.get_user_input()
if user_input:
    chat_service.process_user_input(user_input)