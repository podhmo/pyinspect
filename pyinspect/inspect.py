import ast
import textwrap
from inspect import (
    signature,
    classify_class_attrs,
    getsource,
)
from collections import (
    namedtuple,
    defaultdict,
)
from logging import getLogger as get_logger

logger = get_logger(__name__)
INDENT_PREFIX = '    '


def _indent(text, prefix=INDENT_PREFIX):
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


def find_calling_structure(cls, methods, *, method_owners=("self", "cls")):
    calling_structure = {k: [] for k, _ in methods}
    seen_dict = defaultdict(set)  # for dedup
    for target_method_name, kind in methods:
        candidates = calling_structure[target_method_name]
        seen = seen_dict[target_method_name]
        try:
            source_code = textwrap.dedent(getsource(getattr(cls, target_method_name)))
        except TypeError as e:
            logger.info(repr(e))
            continue

        t = ast.parse(source_code)

        for node in ast.walk(t):
            if isinstance(node, ast.Attribute):
                if not hasattr(node.value, "id"):
                    continue
                if node.attr in calling_structure and node.value.id in method_owners:
                    if node.attr in seen:
                        continue
                    seen.add(node.attr)
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
    calling_structure = find_calling_structure(this_cls, methods)

    def _iterate_methods_with_changing_order():
        used = set()
        rdeps = defaultdict(list)
        for name, callings in calling_structure.items():
            for subname in callings:
                rdeps[subname].append(name)

        for name, kind in methods:
            is_toplevel = name not in rdeps
            if is_toplevel:
                used.add(name)
                yield name, kind

        for name, kind in methods:
            if name in used:
                continue
            used.add(name)
            yield name, kind

    seen = set()
    kind_mapping = {name: kind for name, kind in methods}

    def _create_description_recursively(name, kind, *, history, level=1):
        if name in history:
            return
        history.append(name)
        seen.add(name)
        prefix = ", OVERRIDE" if any(c for c in this_cls.mro()[1:] if hasattr(c, name)) else ""

        try:
            content = doc(name, getattr(this_cls, name))
        except ValueError as e:
            logger.info(e)
            return

        description = "[{kind}{prefix}] {content}".format(prefix=prefix, kind=kind, content=content)

        yield _indent(description, prefix=f"{level:02}:{INDENT_PREFIX * level}")
        for subname in calling_structure[name]:
            subkind = kind_mapping[subname]
            subhistory = history[:]
            yield from _create_description_recursively(
                subname, subkind, history=subhistory, level=level + 1
            )

    method_docs = []
    for name, kind in _iterate_methods_with_changing_order():
        if name in seen:
            continue
        method_docs.extend(_create_description_recursively(name, kind, history=[]))

    relation = " <- ".join([f"00:{cls.__module__}.{cls.__name__}" for cls in this_cls.mro()])
    body = "\n".join(method_docs)
    return "\n".join([relation, body]).rstrip("\n")


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
