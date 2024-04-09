from typing import Optional

from .enachedString import EnhancedStr


class Variable:
    name: str = ""
    description: Optional[EnhancedStr] = None
    of_type: Optional[str] = None
    default_value: Optional[str] = None

    def __init__(self, name: str = ""):
        self.name = name

    def add_description(self, description: EnhancedStr):
        self.description = description

    def add_type(self, of_type: str):
        self.of_type = of_type

    def add_default_value(self, default_value: str):
        self.default_value = default_value

    def __dict__(self):
        return {
            "name": self.name,
            "description": self.description.__dict__() if self.description is not None else None,
            "of_type": self.of_type,
            "default_value": self.default_value
        }