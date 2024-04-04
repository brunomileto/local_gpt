import streamlit as st

from models.GPT import GPTModel
from services.gpt_session_state_service import GPTSessionStateService

class GPTService:
  def __init__(self, gpt_session_state_service:GPTSessionStateService) -> None:
    self.gpt_state = gpt_session_state_service
  
  def render_sidebar_controls(self):
    new_button = st.button("Criar novo GPT")
    if new_button:
      self.render_new_gpt()
    gpts = [f"{key}" for key in sorted(self.gpt_state.gpts.keys())]
    gpts_convo_list = st.radio("GPTs", gpts)
    if ()
    
  def validate_new_gpt(self, gpt:GPTModel):
    if not gpt.name:
      st.info("Informe o nome do gpt")
      st.stop()
    if not gpt.prompt:
      st.info("Informe o prompt")
      st.stop()
    if not self.gpt_state.validate_gpt_creation(gpt):
      st.info("Não foi possível criar este gpt.")
      st.stop()
    return True
  
  def render_new_gpt(self):
    gpt_name = st.text_input("Informe um nome para o gpt", key="gpt_name_input")
    gpt_prompt = st.text_area("Insira o prompt", key="gpt_prompt_text_area", height=600)
    gpt_save = st.button("Salvar")
    if gpt_name and gpt_prompt:
      new_gpt = GPTModel(gpt_name, gpt_prompt)   
      if gpt_save and self.validate_new_gpt(new_gpt):
        self.gpt_state.create_gpt(new_gpt)
        
  def render_gpt(self, gpt_name:str):
          
  
    
  