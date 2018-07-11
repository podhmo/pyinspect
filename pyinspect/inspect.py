from inspect import signature, classify_class_attrs
from logging import getLogger as get_logger
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


def shape_text(this_cls, skip_special_method=False, skip_private_method=False):
    attrs = [
        (name, kind) for name, kind, cls, _ in classify_class_attrs(this_cls) if cls == this_cls
    ]

    if skip_special_method:
        attrs = [
            (name, kind) for name, kind in attrs
            if not (name.startswith("__") and name.endswith("__"))
        ]

    if skip_private_method:
        attrs = [
            (name, kind) for name, kind in attrs if not name.startswith("_") or name.endswith("__")
        ]
    method_docs = []
    for name, kind in attrs:
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


def inspect(target, io=None, skip_special_method=False, skip_private_method=False, only_this=False):
    for cls in target.mro():
        if cls == object:
            break
        text = shape_text(
            cls, skip_special_method=skip_special_method, skip_private_method=skip_private_method
        )
        print(text, file=io)
        if only_this:
            break
