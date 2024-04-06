from typing import Dict
from models.GPT import GPTModel
from services.session_state_service import SessionStateService

class GPTSessionStateService:
  GPTS:str = 'gpt_gpts'
  GPT:str = 'gpt_gpt'
  def __init__(self, session_state: SessionStateService) -> None:
    self.session_state = session_state
    
  def save_gpt(self, new_gpt:GPTModel):
    gpts:Dict[str,str] = self.session_state.get(self.GPTS)
    if gpts:
      gpts[new_gpt.name] = new_gpt.prompt
    else:
      gpts = {new_gpt.name: new_gpt.prompt}
    self.session_state.set(self.GPTS, gpts)
    self.clear_gpt()
    
  def clear_gpt(self):
    self.session_state.set(self.GPT, GPTModel('',''))
  
  @property
  def gpts(self) -> Dict[str, str]|None:
    gpts:Dict[str,str] = self.session_state.get(self.GPTS)
    return gpts