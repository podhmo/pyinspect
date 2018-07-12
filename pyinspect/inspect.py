import ast
import textwrap
from inspect import signature, classify_class_attrs, getsource
from logging import getLogger as get_logger
from collections import namedtuple

logger = get_logger(__name__)


def _indent(text, prefix='    '):
    """Indent text by prepending a given prefix to each line."""
    if not text:
        return ''
    lines = [prefix + line for line in text.split('\n')]
    if lines:
        lines[-1] = lines[-1].rstrip()
    return '\n'.join(lines)


def doc(name, ob):
    # pydoc.plaintext.doc(ob)
    return f"{name}{signature(ob)}"


class Options(namedtuple("Option", "skip_special_method, skip_private_method, only_this")):
    def __new__(
        self,
        skip_special_method=False,
        skip_private_method=False,
        only_this=False,
    ):  # todo: using dataclasses?
        return super().__new__(
            self,
            skip_special_method=skip_special_method,
            skip_private_method=skip_private_method,
            only_this=only_this,
        )


def find_calling_structure(cls, methods):
    calling_structure = {k: [] for k, _ in methods}
    for target_method_name, kind in methods:
        candidates = calling_structure[target_method_name]

        source_code = textwrap.dedent(getsource(getattr(cls, target_method_name)))
        t = ast.parse(source_code)
        for node in ast.walk(t):
            if isinstance(node, ast.Attribute):
                if node.value.id == "self" and node.attr in calling_structure:
                    candidates.append(node.attr)
    return calling_structure


def collect_methods(this_cls, options):
    methods = [
        (name, kind) for name, kind, cls, _ in classify_class_attrs(this_cls)
        if cls == this_cls and "method" in kind
    ]

    if options.skip_special_method:
        methods = [
            (name, kind) for name, kind in methods
            if not (name.startswith("__") and name.endswith("__"))
        ]

    if options.skip_private_method:
        methods = [
            (name, kind) for name, kind in methods
            if not name.startswith("_") or name.endswith("__")
        ]
    return methods


def shape_text(this_cls, methods):
    method_docs = []
    for name, kind in methods:
        if "method" not in kind:
            continue
        prefix = ", OVERRIDE" if any(c for c in this_cls.mro()[1:] if hasattr(c, name)) else ""

        try:
            content = doc(name, getattr(this_cls, name))
        except ValueError as e:
            logger.info(e)
            continue

        method_docs.append(
            "[{kind}{prefix}] {content}".format(prefix=prefix, kind=kind, content=content)
        )

    content = _indent("\n".join(method_docs))
    relation = " <- ".join([f"{cls.__module__}.{cls.__name__}" for cls in this_cls.mro()])
    return "\n".join([relation, content]).rstrip("\n")


def inspect(target, *, options, io=None):
    for cls in target.mro():
        if cls == object:
            break
        methods = collect_methods(cls, options=options)
        text = shape_text(cls, methods)

        print(text, file=io)
        print("", file=io)

        if options.only_this:
            break
