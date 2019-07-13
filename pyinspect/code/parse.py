import logging
from pycomment.parse import (  # noqa
    parse_string,
    parse_file,
    node_name,
    PyTreeVisitor,  # todo: optimization, walk
)
from lib2to3.pgen2 import token  # noqa
from lib2to3.pytree import Node, Leaf  # noqa
from lib2to3.fixer_util import find_indentation  # noqa


class Visitor(PyTreeVisitor):
    logger = logging.getLogger(__name__)
