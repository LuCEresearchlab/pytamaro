from docutils.writers import Writer
from sphinx.util import logging

from .translator import JSONTranslator

logger = logging.getLogger(__name__)


class JSONWriter(Writer):
    output = None

    translator_class = JSONTranslator

    def __init__(self, builder=None):
        # logger.warning('Initializing JSONWriter', color='green')
        super().__init__()
        self.builder = builder

    def translate(self):
        visitor = self.builder.create_translator(self.document, self.builder)
        self.document.walkabout(visitor)
        self.output = visitor.astext()
