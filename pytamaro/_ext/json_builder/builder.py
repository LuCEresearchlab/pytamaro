import os
from contextlib import contextmanager
from typing import Set

from docutils import nodes
from docutils.io import StringOutput
from sphinx.application import Sphinx
from sphinx.builders import Builder
from sphinx.environment import BuildEnvironment
from sphinx.locale import __
from sphinx.util import logging
from sphinx.util.osutil import os_path, ensuredir

from .translator import JSONTranslator
from .writer import JSONWriter

logger = logging.getLogger(__name__)


@contextmanager
def io_handler(file_path: str, log_error=True):
    try:
        yield
    except (IOError, OSError) as err:
        if log_error:
            logger.warning(__("error accessing file %s: %s"), file_path, err)


def get_mod_time(file_path, log_error=True):
    with io_handler(file_path, log_error):
        return os.path.getmtime(file_path)


class JSONBuilder(Builder):
    name = "customJson"
    format = "json"
    epilog = __("The JSON files are in %(outdir)s.")

    allow_parallel = True

    out_suffix = ".json"

    default_translator_class = JSONTranslator  # TODO: implement the translator (Phase 1/3)

    def __init__(self, app: Sphinx, env: BuildEnvironment = None):
        # logger.info('Initializing JSONBuilder', color='green')
        super().__init__(app, env)
        self.writer = None
        self.sec_numbers = None
        self.current_doc_name = None

    def init(self):
        self.sec_numbers = {}

    def get_target_uri(self, docname: str, typ: str = None):
        """
        Returns the target file name.
        """
        # logger.info(f"get_target_uri ({docname})", color='green')
        return f"{docname}{self.out_suffix}"

    def get_outdated_docs(self):
        """
        Return a list of the doc names that have been updated after the last run of this builder.
        """
        for doc_name in self.env.found_docs:
            if doc_name not in self.env.all_docs:
                yield doc_name
                continue

            source_path = self.env.doc2path(doc_name)
            target_path = os.path.join(self.outdir, doc_name + self.out_suffix)
            source_mod_time = get_mod_time(source_path)
            target_mod_time = get_mod_time(target_path, log_error=False)
            if source_mod_time is None or target_mod_time is None or source_mod_time > target_mod_time:
                yield doc_name

    def prepare_writing(self, docnames: Set[str]):
        """
        Select and initiate the Writer for this builder
        """
        # logger.info("prepare_writing.", color='green')

        # Remove API page from the list of docnames since they are not needed in the JSON output
        to_be_removed = []
        for doc_name in docnames:
            if "API" in doc_name:  # or doc_name == "index":
                to_be_removed.append(doc_name)

        for doc_name in to_be_removed:
            docnames.remove(doc_name)

        self.writer = JSONWriter(self)

    def write_doc(self, docname: str, doctree: nodes.document):

        if docname == "index":
            # Remove the index page from the output files since it is not needed in the JSON output because it will
            # create duplication of the Type "Point" already present in the "points" (for the English version) pages
            return
        self.current_doc_name = docname
        self.sec_numbers = self.env.toc_secnumbers.get(docname, {})
        out_filename = os.path.join(self.outdir, f"{os_path(docname)}{self.out_suffix}")

        assert self.writer is not None
        destination = StringOutput(encoding="utf-8")
        self.writer.write(doctree, destination)

        ensuredir(os.path.dirname(out_filename))

        with io_handler(out_filename):
            with open(out_filename, "w", encoding="utf-8") as file:
                file.write(self.writer.output)
