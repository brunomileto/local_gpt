from enum import Enum, unique
from typing import List, Optional

@unique
class EnumAiModels(Enum):
  GPT_4_TURBO = ("Gpt 4 Turbo ($0,004)", "gpt-4-1106-preview")
  GPT_3_5_TURBO = ("Gpt 3.5 Turbo ($0,002)", "gpt-3.5-turbo-0125")

  def __init__(self, description:str, model_name: str) -> None:
    self._description = description
    self._model_name = model_name
  
  @property
  def description(self) -> str:
    return self._description

  @property
  def model_name(self) -> str:
    return self._model_name
  
  @classmethod
  def all_descriptions(cls) -> List[str]:
    return [model.description for model in cls]
  
  @classmethod
  def get_model_by_description(cls, description:str) -> Optional['EnumModels']:
    for model in cls:
      if model.description == description:
        return model
    return None