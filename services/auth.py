import os
import streamlit as st

class AuthService:
  
  auth_key:str = 'authenticated'
  
  def __init__(self) -> None:
    self._initialize_session_state()
  
  def _initialize_session_state(self):
    st.session_state[self.auth_key] = False
  
  def is_authenticated(self) -> bool:
    if self.auth_key not in st.session_state:
      self._initialize_session_state()
    return st.session_state[self.auth_key]
  
  def verify_auth(self) -> None:
    if not self.is_authenticated():
      st.error("Você não está logado")
      st.stop()

  def authenticate(self, user:str, password:str) -> bool:
    correct_username = os.getenv("USERNAME")
    correct_password = os.getenv("PASSWORD")
    authenticated = user == correct_username and password == correct_password
    if authenticated:
      st.session_state[self.auth_key] = authenticated
      return self.is_authenticated()
    else:
      st.error("Incorrect username or password.")
    return False


auth_service = AuthService()