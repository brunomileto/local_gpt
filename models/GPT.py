class GPTModel:  
  def __init__(self, name:str, prompt:str) -> None:
    self._gpt_name = name
    self._gpt_prompt = prompt
  
  @property
  def name(self) -> str:
    return self._gpt_name
  
  @name.setter
  def name(self, value:str) -> None:
    if not isinstance(value, str):
      raise ValueError("GPT name must be a string")
    self._gpt_name = value
  
  @property
  def prompt(self) -> str:
    return self._gpt_prompt
  
  @prompt.setter
  def prompt(self, value:str) -> None:
    if not isinstance(value, str):
      raise ValueError("GPT prompt must be a string")
    self._gpt_prompt = value
      