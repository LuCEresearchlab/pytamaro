from typing import Optional

from .enachedString import EnhancedStr
from .function import Function
from .variable import Variable


class Class:
    name: str = ""
    description: Optional[EnhancedStr] = None

    public_attributes: Optional[list[Variable]] = None
    private_attributes: Optional[list[Variable]] = None
    const_attributes: Optional[list[Variable]] = None

    public_methods: Optional[list[Function]] = None
    private_methods: Optional[list[Function]] = None
    static_methods: Optional[list[Function]] = None

    def __init__(self, name: str = ""):
        self.name = name

    def add_description(self, description: EnhancedStr):
        self.description = description

    def add_attribute(self, attribute: Variable, attribute_type: str = "public"):
        if attribute_type == "public":
            if self.public_attributes is None:
                self.public_attributes = []
            self.public_attributes.append(attribute)
        elif attribute_type == "private":
            if self.private_attributes is None:
                self.private_attributes = []
            self.private_attributes.append(attribute)
        elif attribute_type == "const":
            if self.const_attributes is None:
                self.const_attributes = []
            self.const_attributes.append(attribute)
        else:
            raise ValueError("Invalid type")

    def add_method(self, method: Function, method_type: str = "public"):
        if method_type == "public":
            if self.public_methods is None:
                self.public_methods = []
            self.public_methods.append(method)
        elif method_type == "private":
            if self.private_methods is None:
                self.private_methods = []
            self.private_methods.append(method)
        elif method_type == "static":
            if self.static_methods is None:
                self.static_methods = []
            self.static_methods.append(method)
        else:
            raise ValueError("Invalid type")

    def __dict__(self):
        return {
            "name": self.name,
            "description": self.description.__dict__() if self.description is not None else None,
            "public_attributes": [attr.__dict__() for attr in
                                  self.public_attributes] if self.public_attributes is not None else None,
            "private_attributes": [attr.__dict__() for attr in
                                   self.private_attributes] if self.private_attributes is not None else None,
            "const_attributes": [attr.__dict__() for attr in
                                 self.const_attributes] if self.const_attributes is not None else None,
            "public_methods": [method.__dict__() for method in
                               self.public_methods] if self.public_methods is not None else None,
            "private_methods": [method.__dict__() for method in
                                self.private_methods] if self.private_methods is not None else None,
            "static_methods": [method.__dict__() for method in
                               self.static_methods] if self.static_methods is not None else None
        }
