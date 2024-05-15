from typing import Optional

from .enachedString import EnhancedString


class Variable:
    name: str = ""
    description: Optional[EnhancedString] = None
    of_type: Optional[str] = None
    default_value: Optional[str] = None

    def __init__(self, name: str = ""):
        self.name = name

    def set_name(self, name: str):
        self.name = name

    def add_description(self, description: EnhancedString):
        self.description = description

    def add_type(self, of_type: str):
        self.of_type = of_type

    def add_default_value(self, default_value: str):
        self.default_value = default_value

    def __dict__(self):
        result: dict[str, str | dict] = {"name": self.name}
        if self.description is not None:
            result["description"] = self.description.__dict__()
        if self.of_type is not None:
            result["type"] = self.of_type
        if self.default_value is not None:
            result["default_value"] = self.default_value
        return result
