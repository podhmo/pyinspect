import sys
import os.path


def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser()
    parser.print_usage = parser.print_help  # hack

    parser.add_argument("--here", default=None)

    subparsers = parser.add_subparsers(dest="subcommand")
    subparsers.required = True

    resolve_parser = subparsers.add_parser(resolve.__name__)
    resolve_parser.set_defaults(fn=resolve)
    resolve_parser.add_argument("module_list", nargs="*")

    list_parser = subparsers.add_parser(list.__name__)
    list_parser.set_defaults(fn=list)
    list_parser.add_argument("module", nargs="?", default=None)
    list_parser.add_argument("-d", "--delimiter", default="\t")
    list_parser.add_argument("--where", action="store_true")

    inspect_cmd_parser = subparsers.add_parser(inspect.__name__)
    inspect_cmd_parser.set_defaults(fn=inspect)
    inspect_cmd_parser.add_argument("target_list", nargs="+")
    inspect_cmd_parser.add_argument("--only-this", action="store_true")
    inspect_cmd_parser.add_argument("--all", action="store_true")
    inspect_cmd_parser.add_argument("-n", "--show-level", action="store_true")
    inspect_cmd_parser.add_argument(
        "--skip-special-method", action="store_true", help="skip __foo__()"
    )
    inspect_cmd_parser.add_argument(
        "--skip-private-method", action="store_true", help="skip _foo()"
    )

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
            filepath = filepath[:-len("/__init__.py")]
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
    def _walk_packages(path=None, prefix='', onerror=None, is_ignore=is_ignore):
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
                    path = getattr(sys.modules[info.name], '__path__', None) or []

                    # don't traverse path items we've seen before
                    path = [p for p in path if not seen(p)]

                    yield from _walk_packages(path, info.name + '.', onerror)

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
            [pkgutil.ModuleInfo(module_finder=fake_module_finder, name=module, ispkg=False)],
            _walk_packages(m.__path__, prefix=module + ".")
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
    skip_private_method=False
):
    from inspect import isclass, ismodule, isfunction
    from pyinspect.inspect import inspect, inspect_function
    from pyinspect.inspect import Options as inspect_options
    import magicalimport

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
                        print("----------------------------------------", file=sys.stdout)
                    elif isfunction(member):
                        # todo: shared calling_structure
                        if member.__name__.startswith("_"):
                            continue
                        _inspect(member, fn=inspect_function)
                        print("----------------------------------------", file=sys.stdout)
        elif isfunction(target):
            _inspect(target, fn=inspect_function)
        else:
            print(
                f"sorry {path} is not class (type={type(target)}, repr={target})", file=sys.stderr
            )


if __name__ == "__main__":
    main()
