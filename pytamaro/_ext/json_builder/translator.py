from typing import TYPE_CHECKING, Optional

import docutils.nodes
import sphinx.addnodes
from docutils import nodes
from sphinx.util.docutils import SphinxTranslator

import json
from enum import Enum

from .ast.enachedString import EnhancedStr
from .ast.module import Module
from .ast.type import Type
from .ast.function import Function
from .ast.variable import Variable

from sphinx.util import logging

logger = logging.getLogger(__name__)

if TYPE_CHECKING:  # pragma: no cover
    from .builder import JSONBuilder


class Context(Enum):
    NONE = -1
    MODULE = 0
    TYPE = 1
    FUNCTION = 2
    FUNCTION_RETURN = 3
    FUNCTION_PARAMETERS = 4
    VARIABLE = 5


# A new translator class is created foreach file that is being processed.
# The translator traverses each node of the document in order, so it's possible to differentiate between the different
# nodes by the "deep" of that node.

# Node are inside other nodes (example: title contains text)

class JSONTranslator(SphinxTranslator):
    module: Module

    current_type: Optional[Type] = None
    current_function: Optional[Function] = None
    function_variables: Optional[list[Variable]] = None
    current_variable: Optional[Variable] = None

    current_context: Context = Context.NONE

    def __init__(self, document: nodes.document, builder: "JSONBuilder"):
        super().__init__(document, builder)
        self.module = Module()

    # --------------------------------------------------
    #                   TITLE
    # --------------------------------------------------

    def visit_title(self, node):
        self.module.add_name(node.astext())
        self.current_context = Context.MODULE

    # --------------------------------------------------
    #                   PARAGRAPH
    # --------------------------------------------------

    def visit_paragraph(self, node):
        content = EnhancedStr(node.astext())
        if self.current_context == Context.MODULE:
            self.module.add_description(content)

    # --------------------------------------------------
    #                   DESC
    # --------------------------------------------------

    def visit_desc(self, node):
        desc_type = node.attributes["desctype"]
        if desc_type == "class" or desc_type == "attribute":
            self.current_context = Context.TYPE
        elif desc_type == "function":
            self.current_context = Context.FUNCTION
        elif desc_type == "data":
            self.current_context = Context.VARIABLE

    def depart_desc(self, node):
        desc_type = node.attributes["desctype"]
        if (
                desc_type == "class" or desc_type == "attribute") and self.current_context == Context.TYPE and self.current_type:
            self.module.add_class(self.current_type)
            self.current_type = None
        elif desc_type == "function" and self.current_context == Context.FUNCTION and self.current_function:
            if self.function_variables:
                self.current_function.add_positional_args(self.function_variables)
                self.function_variables = None
            self.module.add_global_function(self.current_function)
            self.current_function = None
        elif desc_type == "data" and self.current_context == Context.VARIABLE and self.current_variable:
            self.module.add_global_variable(self.current_variable)
            self.current_variable = None

        self.current_context = Context.NONE

    # --------------------------------------------------
    #                   DESC_SIGNATURE
    # --------------------------------------------------
    def visit_desc_signature(self, node):
        name = node.attributes["fullname"]
        if self.current_context == Context.TYPE:
            self.current_type = Type(name)
        elif self.current_context == Context.FUNCTION:
            self.current_function = Function(name)
        elif self.current_context == Context.VARIABLE:
            self.current_variable = Variable(name)

    # --------------------------------------------------
    #                   DESC_PARAMETERLIST
    # --------------------------------------------------

    def visit_desc_parameterlist(self, node):
        self.function_variables = []

    # --------------------------------------------------
    #                   DESC_PARAMETER
    # --------------------------------------------------
    def visit_desc_parameter(self, node):
        assert self.function_variables is not None
        self.function_variables.append(Variable())

    # --------------------------------------------------
    #                   INLINE
    # --------------------------------------------------
    def visit_inline(self, node):

        if self.current_context == Context.FUNCTION:
            classes = node.attributes["classes"][0]
            content = node.astext()
            assert self.function_variables is not None
            if classes == "n" and self.function_variables[-1].name == "":
                self.function_variables[-1].set_name(content)
            elif classes == "n":
                self.function_variables[-1].add_type(content)
            elif classes == "default_value":
                self.function_variables[-1].add_default_value(content)

    # --------------------------------------------------
    #                   DESC_RETURNS
    # --------------------------------------------------

    def visit_desc_returns(self, node):
        types = node.astext().split(" -> ")[1]
        assert self.current_function is not None
        self.current_function.add_return_type(types)

    # --------------------------------------------------
    #                   DESC_CONTENT
    # --------------------------------------------------

    def visit_desc_content(self, node: sphinx.addnodes.desc_content):
        if self.current_context == Context.TYPE and self.current_type:
            self.current_type.add_description(EnhancedStr(node.astext()))
        elif self.current_context == Context.FUNCTION and self.current_function:
            functionDescription = EnhancedStr("")
            for child in node.children:
                if isinstance(child, docutils.nodes.paragraph):
                    functionDescription.append_content(child.astext())
                elif isinstance(child, docutils.nodes.figure):
                    uri = child.children[0]['uri']
                    caption = child.astext().split("\n\n")[1]
                    functionDescription.add_image(uri, caption)

            self.current_function.add_description(functionDescription)
        elif self.current_context == Context.VARIABLE and self.current_variable:
            self.current_variable.add_description(EnhancedStr(node.astext().split("\n\n")[0]))

    # --------------------------------------------------
    #                   FIELD
    # --------------------------------------------------
    def depart_field(self, node):
        if self.current_context == Context.FUNCTION_RETURN or self.current_context == Context.FUNCTION_PARAMETERS:
            self.current_context = Context.FUNCTION

    # --------------------------------------------------
    #                   FIELD_NAME
    # --------------------------------------------------
    def visit_field_name(self, node):
        if node.astext() == "Parameters":
            self.current_context = Context.FUNCTION_PARAMETERS
        elif node.astext() == "Returns":
            self.current_context = Context.FUNCTION_RETURN

    # --------------------------------------------------
    #                   FIELD_BODY
    # --------------------------------------------------
    def visit_field_body(self, node):
        if self.current_context == Context.FUNCTION_RETURN and self.current_function:
            self.current_function.add_return_description(node.astext())

    # --------------------------------------------------
    #                   LIST_ITEM
    # --------------------------------------------------
    def visit_list_item(self, node):
        if self.current_context == Context.FUNCTION_PARAMETERS and self.function_variables:
            name = node.astext().split(" ")[0]
            description = ' '.join(node.astext().split(" ")[2:])
            for param in self.function_variables:
                if param.name == name:
                    param.add_description(EnhancedStr(description))
                    break

    # --------------------------------------------------
    #                   UNKNOWN
    # --------------------------------------------------

    def unknown_departure(self, node):
        pass

    def unknown_visit(self, node):
        pass

    # --------------------------------------------------
    #                   OTHER METHODS
    # --------------------------------------------------
    def astext(self):
        return json.dumps(self.module.__dict__())
