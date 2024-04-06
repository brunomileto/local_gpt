import streamlit as st

from models.GPT import GPTModel
from services.gpt_session_state_service import GPTSessionStateService
#
class GPTService:
  def __init__(self, gpt_session_state_service:GPTSessionStateService) -> None:
    self.gpt_state = gpt_session_state_service
    
  @property
  def is_updating(self) -> bool:
    gpts = self.gpt_state.gpts
    if gpts and self.name in gpts.keys():
      return True
    return False  
    
  @property
  def name(self) -> str:
    return st.session_state.get("gpt_name")
  
  @name.setter
  def name(self, value:str) -> None:
    st.session_state.gpt_name = value
  
  @property
  def prompt(self) -> str:
    return st.session_state.get("gpt_prompt")
  
  @prompt.setter
  def prompt(self, value:str) -> None:
    st.session_state.gpt_prompt = value
    
  def render_gpt(self):
    st.text_input("Informe o nome do gpt", key="gpt_name", )
    st.text_area("Informe o prompt", key="gpt_prompt", height=600)
    st.button("Salvar", on_click=self.submit_gpt, disabled= not (self.name and self.prompt))
  
  def submit_gpt(self):
    if self.name and self.prompt:
      gpt = GPTModel(name=self.name, prompt=self.prompt)
      self.gpt_state.save_gpt(gpt)
      if self.is_updating:
        self.reset_gpts_list()
      self.clear_inputs()
  
  def clear_inputs(self):
    st.session_state.gpt_name = ''
    st.session_state.gpt_prompt = ''

  def render_sidebar_controls(self):
    gpts = self.gpt_state.gpts
    if gpts:
      st.radio("GPTs", ["Novo"] + [f"{key}" for key in sorted(gpts.keys())], on_change=self.load_gpt, key='gpts_list')
  
  def reset_gpts_list(self):
    st.session_state.gpts_list = "Novo"
  
  def load_gpt(self):
    key = st.session_state.get("gpts_list")
    if key in self.gpt_state.gpts.keys():
      self.name = key
      self.prompt = self.gpt_state.gpts[key]
    else:
      self.clear_inputs()