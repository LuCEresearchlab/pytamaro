from typing import Optional

from .class_def import Class
from .enachedString import EnhancedStr
from .function import Function
from .variable import Variable


class Module:
    name: str = ""
    description: Optional[EnhancedStr] = None
    classes: Optional[list[Class]] = None
    global_functions: Optional[list[Function]] = None
    global_variables: Optional[list[Variable]] = None

    def __init__(self, name: str = ""):
        self.name = name

    def add_description(self, description: EnhancedStr):
        self.description = description

    def add_class(self, class_: Class):
        if self.classes is None:
            self.classes = []
        self.classes.append(class_)

    def add_global_function(self, function: Function):
        if self.global_functions is None:
            self.global_functions = []
        self.global_functions.append(function)

    def add_global_variable(self, variable: Variable):
        if self.global_variables is None:
            self.global_variables = []
        self.global_variables.append(variable)

    def get_class(self, class_name: str):
        if self.classes is None:
            return None
        for class_ in self.classes:
            if class_.name == class_name:
                return class_
        return None

    def get_global_function(self, function_name: str):
        if self.global_functions is None:
            return None
        for function in self.global_functions:
            if function.name == function_name:
                return function
        return None

    def get_global_variable(self, variable_name: str):
        if self.global_variables is None:
            return None
        for variable in self.global_variables:
            if variable.name == variable_name:
                return variable
        return None

    def __dict__(self):
        return {
            "name": self.name,
            "description": self.description.__dict__() if self.description is not None else None,
            "classes": [class_.__dict__() for class_ in self.classes] if self.classes is not None else None,
            "global_functions": [function.__dict__() for function in
                                 self.global_functions] if self.global_functions is not None else None,
            "global_variables": [variable.__dict__() for variable in
                                 self.global_variables] if self.global_variables is not None else None
        }
