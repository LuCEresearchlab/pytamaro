__version__ = "0.0.1"
__docformat__ = "reStructuredText"

from .builder import JSONBuilder


def setup(app):
    app.add_builder(JSONBuilder)
    app.add_config_value("json_uri_doc_suffix", ".json", False)
