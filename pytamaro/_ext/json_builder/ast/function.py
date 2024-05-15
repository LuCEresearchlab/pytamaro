from typing import Optional

from .enachedString import EnhancedString
from .variable import Variable


class Function:
    name: str = ""
    description: Optional[EnhancedString] = None
    parameters: Optional[list[Variable]] = None
    return_type: Optional[str] = None
    return_description: Optional[str] = None

    def __init__(self, name: str = ""):
        self.name = name

    def add_return_type(self, return_type: str = ""):
        self.return_type = return_type

    def add_return_description(self, description: str = ""):
        self.return_description = description

    def add_parameters(self, param: Variable):
        if self.parameters is None:
            self.parameters = []
        self.parameters.append(param)

    def add_positional_args(self, args: list[Variable]):
        self.parameters = args

    def add_description(self, description: EnhancedString):
        self.description = description

    def __dict__(self):
        result: dict[str, str | dict | list[dict]] = {"name": self.name}
        if self.description is not None:
            result["description"] = self.description.__dict__()
        if self.parameters is not None:
            result["parameters"] = [param.__dict__() for param in self.parameters]
        if self.return_type is not None:
            result["return_type"] = self.return_type
        if self.return_description is not None:
            result["return_description"] = self.return_description
        return result
