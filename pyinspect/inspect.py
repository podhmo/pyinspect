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


def doc(name, kind, ob):
    if kind == "property":
        return f"{name}"

    # pydoc.plaintext.doc(ob)
    try:
        return f"{name}{signature(ob)}"
    except TypeError as e:
        logger.info(repr(e))
        return f"{name}"


class Options(
    namedtuple("Option", "skip_special_method, skip_private_method, show_level, only_this")
):
    def __new__(
        self,
        skip_special_method=False,
        skip_private_method=False,
        show_level=False,
        only_this=False,
    ):  # todo: using dataclasses?
        return super().__new__(
            self,
            skip_special_method=skip_special_method,
            skip_private_method=skip_private_method,
            show_level=show_level,
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
        except OSError as e:
            logger.info("%r (cls=%s, attr=%s)", e, cls.__name__, target_method_name)
            continue
        except TypeError as e:
            logger.info("%r (cls=%s, attr=%s)", e, cls.__name__, target_method_name)
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


def collect_attrs(this_cls, *, options):
    attrs = [
        (name, kind) for name, kind, cls, _ in classify_class_attrs(this_cls)
        if cls == this_cls and ("method" in kind or "property" == kind)
    ]

    if options.skip_special_method:
        attrs = [
            (name, kind) for name, kind in attrs
            if not (name.startswith("__") and name.endswith("__"))
        ]

    if options.skip_private_method:
        attrs = [
            (name, kind) for name, kind in attrs if not name.startswith("_") or name.endswith("__")
        ]
    return attrs


def shape_text(this_cls, attrs, *, options):
    calling_structure = find_calling_structure(this_cls, attrs)

    def _iterate_attrs_toplevel_first_order():
        used = set()
        rdeps = defaultdict(list)
        for name, callings in calling_structure.items():
            for subname in callings:
                rdeps[subname].append(name)

        for name, kind in attrs:
            is_toplevel = name not in rdeps
            if is_toplevel:
                used.add(name)
                yield name, kind

        for name, kind in attrs:
            if name in used:
                continue
            used.add(name)
            yield name, kind

    seen = set()
    kind_mapping = {name: kind for name, kind in attrs}

    def _iterate_with_nested_level(name, kind, *, history, level=1):
        if name in history:
            return
        history.append(name)
        seen.add(name)
        yield name, kind, level
        for subname in calling_structure[name]:
            subkind = kind_mapping[subname]
            subhistory = history[:]
            yield from _iterate_with_nested_level(
                subname, subkind, history=subhistory, level=level + 1
            )

    method_docs = []
    for name, kind in _iterate_attrs_toplevel_first_order():
        if name in seen:
            continue
        for name, kind, level in _iterate_with_nested_level(name, kind, history=[]):
            prefix = ", OVERRIDE" if any(c for c in this_cls.mro()[1:] if hasattr(c, name)) else ""

            try:
                content = doc(name, kind, getattr(this_cls, name))
            except ValueError as e:
                logger.info(e)
                continue

            description = "[{kind}{prefix}] {content}".format(
                prefix=prefix, kind=kind, content=content
            )
            prefix = INDENT_PREFIX * level
            if options.show_level:
                prefix = f"{level:02}:{prefix}"
            method_docs.append(_indent(description, prefix=prefix))

    relation = " <- ".join([f"{cls.__module__}.{cls.__name__}" for cls in this_cls.mro()])
    if options.show_level:
        relation = f"00:{relation}"

    body = "\n".join(method_docs)
    return "\n".join([relation, body]).rstrip("\n")


def inspect(target, *, options, io=None):
    for cls in target.mro():
        if cls == object:
            break
        attrs = collect_attrs(cls, options=options)
        text = shape_text(cls, attrs, options=options)

        print(text, file=io)
        print("", file=io)

        if options.only_this:
            break
