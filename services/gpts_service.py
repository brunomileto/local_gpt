import streamlit as st

from models.GPT import GPTModel
from services.gpt_session_state_service import GPTSessionStateService

class GPTService:
  def __init__(self, gpt_session_state_service:GPTSessionStateService) -> None:
    self.gpt_state = gpt_session_state_service
  
  def load_gpt(self, selected_gpt:str):
    if selected_gpt == 'Atual':
      self.render_new_gpt()
    else:
      self.render_gpt(selected_gpt)
  
  def render_sidebar_controls(self):
    new_button = st.button("Criar novo GPT")
    if new_button:
      self.render_new_gpt()
    
    if (self.gpt_state.gpts):
      gpts = ["Atual"] + [f"{key}" for key in sorted(self.gpt_state.gpts.keys())]
      selected_gpt = st.radio("GPTs", gpts)
      if (selected_gpt != self.gpt_state.selected_gpt):
        self.load_gpt(selected_gpt)
    
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
    gpt = self.gpt_state.get_gpt(gpt_name)
    if not gpt:
      self.render_new_gpt()
    gpt_name = st.text_input("Informe um nome para o gpt", key="gpt_name_input", value=gpt.name)
    gpt_prompt = st.text_area("Insira o prompt", key="gpt_prompt_text_area", height=600, value=gpt.prompt)
    gpt_save = st.button("Salvar")
    if gpt_name and gpt_prompt:
      new_gpt = GPTModel(gpt_name, gpt_prompt)   
      if gpt_save and self.validate_new_gpt(new_gpt):
        self.gpt_state.create_gpt(new_gpt)
  
    
  #TODO: testar renders. A ideia é de uma página somente para criação de gpts(esta), e outra
  # para selecionar e utilizar os gpts