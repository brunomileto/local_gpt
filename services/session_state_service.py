import streamlit as st
from typing import List

class SessionStateService:
  def __init__(self) -> None:
    pass

  @staticmethod
  def keys() -> List[str]:
    return st.session_state.keys()

  @staticmethod
  def get(key:str, default=None):
    return st.session_state.get(key, default=default)

  @staticmethod
  def set(key:str, value) -> None:
    st.session_state[key] = value