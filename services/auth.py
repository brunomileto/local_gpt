from logging import Logger
import os
import streamlit as st
from streamlit_cookies_manager import CookieManager
from streamlit_cookies_manager.encrypted_cookie_manager import EncryptedCookieManager
from services.interfaces.i_db import IDatabase
from services.sqlalchemy_db import SQLAlchemyDatabase



class AuthService:
  auth_key:str = 'authenticated'
  
  def __init__(self, db_service:IDatabase) -> None:
    self.db = db_service
    self.cookies = EncryptedCookieManager(prefix='miletos/local-gpt' ,password="My secret password not soo secret more or lessy")
    if not self.cookies.ready():
      # Wait for the component to load and send us current cookies.
      st.stop()

  def is_authenticated(self) -> bool:
    """Check if user is authenticated in session state"""
    return st.session_state.get(self.auth_key, False) or ('authenticated' in self.cookies.keys() and bool(self.cookies['authenticated']))
  
  def verify_auth(self) -> None:
    """Ensure the user is authenticated, stop app if not"""
    if not self.is_authenticated():
      st.error("Você não está logado")
      st.stop()
  
  def has_auth_cookie(self, username:str) -> bool:
    if 'authenticated' in self.cookies.keys() and bool(self.cookies['authenticated']) and username in self.cookies.items():
        return True
    return False
  
  def set_auth_cookie(self, username:str) -> None:
      self.cookies["username"] = username   
      self.cookies["authenticated"] = 'True'
    
  
  def authenticate(self, username:str, password:str) -> bool:
    """Authenticate user against database."""
    if self.has_auth_cookie(username=username):
      return True
    
    if not self.db.get_user(username=username):
      self.db.create_user(username=username, password=password)             
      st.session_state[self.auth_key] = True
      self.set_auth_cookie(username=username)
      return True  
    
    if self.db.authenticate_user(username=username, password=password):
      st.session_state[self.auth_key] = True
      self.set_auth_cookie(username=username)
      return True
    
    st.error("Senha incorreta.")
    return False
  
db_service = SQLAlchemyDatabase()
auth_service = AuthService(db_service)