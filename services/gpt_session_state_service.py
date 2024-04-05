from typing import Dict
from models.GPT import GPTModel
from services.session_state_service import SessionStateService

class GPTSessionStateService:
  GPTS:str = 'gpt_created_gpts'
  SELECTED_GPT:str = 'gpt_selected_gpt'
  
  def __init__(self,  session_state_service: SessionStateService) -> None:
    self.state_service = session_state_service
  
  def get_gpt(self, gpt_name:str) -> GPTModel:
    gpts = self.gpts
    if not gpt_name in gpts.keys():
      return None
    gpt = GPTModel(gpt_name, gpts[gpt_name])
    return gpt
    
  @property
  def gpts(self) -> Dict[str, str]:
    gpts = self.state_service.get(self.GPTS)
    if not gpts:
      return gpts
    return gpts
  #TODO: Preciso criar lógica para selecionar o gpt atual, do radio button
  # para evitar problemas no carregamento do sidebar
  # gpt selecionado, precisa ser diferente do gpts_convo_list para carregar um novo gpt na tela
  @property
  def selected_gpt(self) -> str:
    return self.state_service.get(self.SELECTED_GPT)
  
  @selected_gpt.setter
  def selected_gpt(self, value:str) -> None:
    gpts = self.gpts
    if value not in gpts.keys():
      raise ValueError("gpt must exists")
    self.state_service.set(self.SELECTED_GPT, value)
  
  def create_gpt(self, gpt:GPTModel) -> None:
    gpts = self.state_service.get(self.GPTS)
    if not gpts:
      gpts = {gpt.name: gpt.prompt}
    else:
      gpts[gpt.name] = gpt.prompt
    self.state_service.set(self.GPTS, gpts)
        
  def validate_gpt_creation(self, gpt:GPTModel) -> bool:
    gpts = self.state_service.get(self.GPTS)
    if gpts:
      if self.gpts.get(gpt.name):
        return False  
    return True