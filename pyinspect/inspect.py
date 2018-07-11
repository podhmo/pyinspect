import pydoc
import re


def shape_text(this_cls, doc=pydoc.plaintext, skip_special_method=False, skip_private_method=False):
    attrs = [
        (name, kind) for name, kind, cls, _ in pydoc.classify_class_attrs(this_cls)
        if cls == this_cls
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
    method_docs = [
        "[{kind}{prefix}] {doc}".format(
            prefix=", OVERRIDE" if any(c for c in this_cls.mro()[1:] if hasattr(c, name)) else "",
            kind=kind,
            doc=doc.document(getattr(this_cls, name))
        ) for name, kind in attrs if "method" in kind
    ]

    content = doc.indent("".join(method_docs))
    relation = " <- ".join([f"{cls.__module__}.{cls.__name__}" for cls in this_cls.mro()])
    return "\n".join([relation, content])


def grep_by_indent(s, level, rx=re.compile("^\s+")):
    for line in s.split("\n"):
        m = rx.search(line)
        if m is None or len(m.group(0)) <= level:
            yield line


def inspect(target, io=None, skip_special_method=False, skip_private_method=False, only_this=False):
    for cls in target.mro():
        if cls == object:
            break
        text = shape_text(
            cls, skip_special_method=skip_special_method, skip_private_method=skip_private_method
        )
        print("\n".join(grep_by_indent(text, 4)), file=io)
        if only_this:
            break
