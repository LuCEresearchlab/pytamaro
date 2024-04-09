from typing import Optional

from .enachedString import EnhancedStr
from .variable import Variable


class Function:
    name: str = ""
    description: Optional[EnhancedStr] = None
    positional_args: Optional[list[Variable]] = None
    arbitrary_arg: Optional[str] = None
    arbitrary_keyword_arg: Optional[str] = None
    return_type: Optional[str] = None
    body: str = "" # TODO: remove

    def __init__(self, name: str = ""):
        self.name = name

    def add_body(self, body: str = ""):
        self.body = body

    def add_return_type(self, return_type: str = ""):
        self.return_type = return_type

    def add_positional_arg(self, arg: Variable):
        if self.positional_args is None:
            self.positional_args = []
        self.positional_args.append(arg)

    def add_arbitrary_arg(self, arg: str):
        self.arbitrary_arg = arg

    def add_arbitrary_keyword_arg(self, arg: str):
        self.arbitrary_keyword_arg = arg

    def add_description(self, description: EnhancedStr):
        self.description = description

    def __dict__(self):
        return {
            "name": self.name,
            "description": self.description.__dict__() if self.description is not None else None,
            "positional_args": [arg.__dict__() for arg in self.positional_args] if self.positional_args is not None else None,
            "arbitrary_arg": self.arbitrary_arg,
            "arbitrary_keyword_arg": self.arbitrary_keyword_arg,
            "return_type": self.return_type,
            "body": self.body
        }