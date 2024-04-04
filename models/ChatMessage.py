from enums.EnumChatRoles import EnumChatRoles


class ChatMessage:
    def __init__(self, role: EnumChatRoles, content: str) -> None:
        self._role:EnumChatRoles = role
        self._content = content
    
    @property
    def role(self) -> str:
        """Getter for the role property."""
        return self._role.value

    @role.setter
    def role(self, value: EnumChatRoles) -> None:
        """Setter for the role property with basic validation."""
        if not isinstance(value, EnumChatRoles):
            raise ValueError("Role must be a EnumChatRoles.")
        self._role = value

    @property
    def content(self) -> str:
        """Getter for the content property."""
        return self._content

    @content.setter
    def content(self, value: str) -> None:
        """Setter for the content property with basic validation."""
        if not isinstance(value, str):
            raise ValueError("Content must be a string.")
        self._content = value

    def __repr__(self) -> str:
        """String representation of the Message object for debugging."""
        return f"Message(role='{self._role.value}', content='{self._content}')"
    
    def to_dict(self) -> dict:
        return {'role': self.role.lower(), 'content': self.content}
