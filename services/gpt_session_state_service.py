from typing import Dict
from models.GPT import GPTModel
from services.session_state_service import SessionStateService

class GPTSessionStateService:
  GPTS:str = 'gpt_created_gpts'
  
  def __init__(self,  session_state_service: SessionStateService) -> None:
    self.state_service = session_state_service
  
  
  #TODO: Preciso criar lógica para selecionar o gpt atual, do radio button
  # para evitar problemas no carregamento do sidebar
  # gpt selecionado, precisa ser diferente do gpts_convo_list para carregar um novo gpt na tela
  def selected_gpt(self):
    pass
  
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
    
  @property
  def gpts(self) -> Dict[str, str]:
    gpts = self.state_service.get(self.GPTS)
    if not gpts:
      return gpts
    return gpts