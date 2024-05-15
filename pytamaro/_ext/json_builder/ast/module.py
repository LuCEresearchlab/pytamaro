from typing import Optional

from .type import Type
from .enachedString import EnhancedString
from .function import Function
from .variable import Variable


class Module:
    name: str = ""
    description: Optional[EnhancedString] = None
    types: Optional[list[Type]] = None
    global_functions: Optional[list[Function]] = None
    global_variables: Optional[list[Variable]] = None

    def add_name(self, name):
        self.name = name

    def add_description(self, description: EnhancedString):
        self.description = description

    def add_class(self, class_: Type):
        if self.types is None:
            self.types = []
        self.types.append(class_)

    def add_global_function(self, function: Function):
        if self.global_functions is None:
            self.global_functions = []
        self.global_functions.append(function)

    def add_global_variable(self, variable: Variable):
        if self.global_variables is None:
            self.global_variables = []
        self.global_variables.append(variable)

    def get_class(self, class_name: str):
        if self.types is None:
            return None
        for class_ in self.types:
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
        result: dict[str, str | dict | list[dict]] = {"name": self.name}
        if self.description is not None:
            result["description"] = self.description.__dict__()
        if self.types is not None:
            result["types"] = [type_.__dict__() for type_ in self.types]
        if self.global_functions is not None:
            result["functions"] = [function.__dict__() for function in self.global_functions]
        if self.global_variables is not None:
            result["variables"] = [variable.__dict__() for variable in self.global_variables]
        return result
