from typing import Optional

from .enachedString import EnhancedString
from .function import Function
from .variable import Variable


# TODO: change this into "type" to make it usable both as "class" and "attribute" due to the semplification we do given
#  our use case of this ast.

# TODO: remove **_attributes and **_methods since in PyTamaro those are not used since classes are used only as types
#   for the parameter and returned value of the defined functions

class Type:
    name: str = ""
    description: Optional[EnhancedString] = None

    def __init__(self, name: str = ""):
        self.name = name

    def add_description(self, description: EnhancedString):
        self.description = description

    def __dict__(self):
        result: dict[str, str | dict] = {"name": self.name}
        if self.description is not None:
            result["description"] = self.description.__dict__()
        return result
