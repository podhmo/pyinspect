import sys
import os.path


def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser()
    parser.print_usage = parser.print_help  # hack

    parser.add_argument("--here", default=None)

    subparsers = parser.add_subparsers(dest="subcommand")
    subparsers.required = True

    # resolve
    sparser = subparsers.add_parser(resolve.__name__)
    sparser.set_defaults(fn=resolve)
    sparser.add_argument("module_list", nargs="*")
    sparser = None

    # list
    sparser = subparsers.add_parser(list.__name__)
    sparser.set_defaults(fn=list)
    sparser.add_argument("module", nargs="?", default=None)
    sparser.add_argument("-d", "--delimiter", default="\t")
    sparser.add_argument("--where", action="store_true")
    sparser = None

    # inspect
    sparser = subparsers.add_parser(inspect.__name__)
    sparser.set_defaults(fn=inspect)
    sparser.add_argument("target_list", nargs="+")
    sparser.add_argument("--only-this", action="store_true")
    sparser.add_argument("--all", action="store_true")
    sparser.add_argument("-n", "--show-level", action="store_true")
    sparser.add_argument(
        "--skip-special-method", action="store_true", help="skip __foo__()"
    )
    sparser.add_argument(
        "--skip-private-method", action="store_true", help="skip _foo()"
    )
    sparser = None

    # parse
    sparser = subparsers.add_parser(parse.__name__)
    sparser.set_defaults(fn=parse)
    sparser.add_argument("sources", nargs="+")
    sparser = None

    # quote
    sparser = subparsers.add_parser(quote.__name__)
    sparser.set_defaults(fn=quote)
    sparser.add_argument("source", help="<filename or module path>(:L?<lineno>)?")
    sparser.add_argument("--lineno", type=int)
    sparser.add_argument("--show-lineno", action="store_true")
    sparser.add_argument(
        "-f", "--format", choices=["markdown", "raw"], default="markdown"
    )
    sparser.add_argument(
        "-s", "--without-filename", action="store_false", dest="show_filename"
    )
    sparser.add_argument("-n", type=int, default=2)
    sparser = None

    args = parser.parse_args(argv)
    params = vars(args).copy()

    # support relative
    sys.path.append(params.pop("here") or os.getcwd())

    params.pop("subcommand")
    params.pop("fn")(**params)


def resolve(*, module_list):
    from importlib.util import find_spec

    itr = module_list or (line.rstrip("\n") for line in sys.stdin)

    for module in itr:
        spec = find_spec(module)
        if spec is None:
            continue
        filepath = spec.origin
        if filepath is None:
            continue
        if filepath.endswith("/__init__.py"):
            filepath = filepath[: -len("/__init__.py")]
        print(filepath)


def list(*, module=None, where=False, delimiter=", ", is_ignore=None):
    import pkgutil
    import itertools
    import magicalimport
    from importlib import import_module

    if is_ignore is None:

        def is_ignore(name):
            return "._" in name or name.endswith(".tests")

    # valiant of pkgutil.walk_packags
    def _walk_packages(path=None, prefix="", onerror=None, is_ignore=is_ignore):
        def seen(p, m={}):
            if p in m:
                return True
            m[p] = True

        for info in pkgutil.iter_modules(path, prefix):
            if is_ignore(info.name):
                continue
            yield info

            if info.ispkg:
                try:
                    import_module(info.name)
                except ImportError:
                    if onerror is not None:
                        onerror(info.name)
                except Exception:
                    if onerror is not None:
                        onerror(info.name)
                    else:
                        raise
                else:
                    path = getattr(sys.modules[info.name], "__path__", None) or []

                    # don't traverse path items we've seen before
                    path = [p for p in path if not seen(p)]

                    yield from _walk_packages(path, info.name + ".", onerror)

    if module is None:
        iterator = (sm for sm in pkgutil.iter_modules() if not sm.name.startswith("_"))
    else:
        try:
            m = magicalimport.import_module(module)
        except ModuleNotFoundError as e:
            print(e, file=sys.stderr)
            sys.exit(1)

        if not hasattr(m, "__path__"):
            return

        class fake_module_finder:
            _path_cache = []
            path = getattr(m, "__file__", None)

        iterator = itertools.chain(
            [
                pkgutil.ModuleInfo(
                    module_finder=fake_module_finder, name=module, ispkg=False
                )
            ],
            _walk_packages(m.__path__, prefix=module + "."),
        )

    for sm in iterator:
        row = [sm.name]

        if where:
            fname = "__init__.py"
            module_name = sm.name.split(".")[-1]
            for guessed_fname in sm.module_finder._path_cache:
                base, ext = os.path.splitext(guessed_fname)
                if base == module_name:
                    if not ext:
                        fname = os.path.join(guessed_fname, "__init__.py")
                    else:
                        fname = guessed_fname

            row.append(os.path.join(sm.module_finder.path, fname))
        print(delimiter.join(row))


def inspect(
    *,
    target_list,
    only_this=False,
    all=False,  # xxx: bultins.all is shadowed
    show_level=False,
    skip_special_method=False,
    skip_private_method=False,
):
    from inspect import isclass, ismodule, isfunction
    import magicalimport
    from .inspect import inspect, inspect_function
    from .inspect import Options as inspect_options

    def _inspect(target, *, fn=inspect):
        return fn(
            target,
            options=inspect_options(
                skip_special_method=skip_special_method,
                skip_private_method=skip_private_method,
                show_level=show_level,
                only_this=only_this,
            ),
            io=sys.stdout,
        )

    for path in target_list:
        try:
            if ":" in path:
                target = magicalimport.import_symbol(path, sep=":")
            else:
                target = magicalimport.import_module(path)
        except ModuleNotFoundError as e:
            print(e, file=sys.stderr)
            continue

        if isclass(target):
            _inspect(target)
        elif ismodule(target):
            builtins = sys.modules["builtins"]
            for member in target.__dict__.values():
                where = getattr(member, "__module__", None)
                if where == builtins:
                    continue

                if all or where == target.__name__:
                    if isclass(member):
                        _inspect(member)
                        print(
                            "----------------------------------------", file=sys.stdout
                        )
                    elif isfunction(member):
                        # todo: shared calling_structure
                        if member.__name__.startswith("_"):
                            continue
                        _inspect(member, fn=inspect_function)
                        print(
                            "----------------------------------------", file=sys.stdout
                        )
        elif isfunction(target):
            _inspect(target, fn=inspect_function)
        else:
            print(
                f"sorry {path} is not class (type={type(target)}, repr={target})",
                file=sys.stderr,
            )


def parse(sources: list) -> None:
    import logging
    import pathlib
    from importlib.util import find_spec
    from .code.parse import parse_file, PyTreeVisitor

    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    for source in sources:
        if pathlib.Path(source).exists():
            filename = source
        else:
            try:
                filename = find_spec(source).loader.get_filename()
            except AttributeError:
                print(f"not found:{source}", file=sys.stderr)
                continue
        t = parse_file(filename)
        v = PyTreeVisitor()
        v.visit(t)


def quote(
    source: str,
    *,
    lineno: int = None,
    n: int,
    show_lineno: bool,
    format: str,
    show_filename: bool,
) -> None:
    """quote code"""
    import pathlib
    import contextlib
    from io import StringIO
    from importlib.util import find_spec
    from .code.quote import run

    o = StringIO()

    @contextlib.contextmanager
    def _submit(filename: str, *, language="python"):
        if show_filename:
            try:
                print(
                    pathlib.Path(filename).relative_to(pathlib.Path(".").absolute()),
                    file=o,
                )
            except ValueError:
                print(filename, file=o)

        if format == "markdown":
            if show_filename:
                print("", file=o)
            print(f"```{language}", file=o)

        yield

        if format == "markdown":
            print("```", file=o)
        print(o.getvalue())

    if ":" in source:
        source, lineno = source.split(":", 1)
        lineno = int(lineno.lstrip("L"))

    if pathlib.Path(source).exists():
        filename = source
    else:
        try:
            filename = find_spec(source).loader.get_filename()
        except AttributeError:
            print(f"not found:{source}", file=sys.stderr)
            sys.exit(1)
    with _submit(filename):
        try:
            run(filename, lineno=lineno, n=n, show_lineno=show_lineno, io=o)
        except RuntimeError as e:
            print(f"runtime error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
