from typing import TYPE_CHECKING

from docutils import nodes
from sphinx.util import logging
from sphinx.util.docutils import SphinxTranslator

from .ast.enachedString import EnhancedStr
from .ast.module import Module
from .ast.class_def import Class
from .ast.function import Function

logger = logging.getLogger(__name__)

import json

if TYPE_CHECKING:  # pragma: no cover
    from .builder import JSONBuilder


# A new translator class is created foreach file that is being processed.
# The translator traverses each node of the document in order so it's possible to differentiate between the different
# nodes by the "deep" of that node.

# Node are inside other nodes (example: title contains text)

# { "filename": "",
#   "description": "",
#   "classes": [{"name": "",
#                "description": "",
#                 "fields": [],
#                 "functions": []}],
# } TODO: clenaup
class JSONTranslator(SphinxTranslator):
    module: Module = None

    current_class: Class = None
    current_function: Function = None

    current_part: str = ""

    def __init__(self, document: nodes.document, builder: "JSONBuilder"):
        logger.info("Translator init.", color='blue')
        super().__init__(document, builder)

    def visit_title(self, node):
        # logger.info(f"Visiting title. {node.astext()}", color='blue')
        self.module = Module(node.astext())
        self.current_part = "module"

    def visit_paragraph(self, node):
        if self.current_part == "module":
            self.module.add_description(EnhancedStr(node.astext()))
        elif self.current_part == "class":
            self.current_class.add_description(EnhancedStr(node.astext()))
        elif self.current_part == "function":
            self.current_function.add_description(EnhancedStr(node.astext()))
        else:
            logger.error(f"Invalid part {self.current_part} for pragragh")

    def visit_desc(self, node):
        desc_type = node.attributes["desctype"]
        if desc_type == "class":
            self.current_part = "class"
        elif desc_type == "function":
            self.current_part = "function"
        elif desc_type == "attribute":
            logger.info(f"Attribute desc{node}", color='green')
        else:
            logger.error(f"Invalid desc type: {desc_type}")

    def depart_desc(self, node):
        desc_type = node.attributes["desctype"]
        if desc_type == "class" and self.current_part == "class":
            self.module.add_class(self.current_class)
        elif desc_type == "function" and self.current_part == "function":
            self.module.add_global_function(self.current_function)
        else:
            logger.error(f"Invalid desc type: {desc_type} or current part: {self.current_part} for departing desc")

    def visit_desc_signature(self, node):
        if self.current_part == "class":
            self.current_class = Class(node.attributes["_toc_name"])
        elif self.current_part == "function":
            self.current_function = Function(node.attributes["_toc_name"])
        else:
            logger.error(f"Invalid part {self.current_part} for desc signature")

    def astext(self):
        return json.dumps(self.module.__dict__())

    def unknown_departure(self, node):
        # logger.info(f"Unknown departure {node}", color='blue')
        pass

    def unknown_visit(self, node):
        # logger.info(f"Unknown departure {node}", color='blue')
        pass
