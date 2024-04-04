from services.gpt_session_state_service import GPTSessionStateService
from services.gpts_service import GPTService
import streamlit as st

from services.session_state_service import SessionStateService

state_service = SessionStateService()
gpt_state_service = GPTSessionStateService(state_service)
gpt_service = GPTService(state_service)

with st.sidebar:
    st.header("GPTs")
    gpt_service.render_sidebar_controls()

gpt_service.render_new_gpt()