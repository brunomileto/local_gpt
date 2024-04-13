import hashlib


class Utils:
  def __init__(self) -> None:
    pass
  
  @staticmethod
  def hash(string:str) -> str:
    return hashlib.sha256(string.encode()).hexdigest()