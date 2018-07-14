import sys
import os.path


def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser()
    parser.print_usage = parser.print_help  # hack

    subparsers = parser.add_subparsers(dest="subcommand")
    subparsers.required = True

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

    list_parser = subparsers.add_parser(list.__name__)
    list_parser.set_defaults(fn=list)
    list_parser.add_argument("module")
    list_parser.add_argument("-d", "--delimiter", default="\t")
    list_parser.add_argument("--where", action="store_true")

    args = parser.parse_args(argv)
    params = vars(args)
    params.pop("subcommand")
    params.pop("fn")(**params)


def list(*, module, where=False, delimiter=", "):
    import importlib
    import pkgutil
    try:
        m = importlib.import_module(module)
    except ModuleNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    row = [module]
    if where:
        if hasattr(row, "__file__"):
            row.append(m.__file__)
    print(delimiter.join(row))

    if not hasattr(m, "__path__"):
        return

    for sm in pkgutil.walk_packages(m.__path__, prefix=module + "."):
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
    from inspect import isclass, ismodule
    from pyinspect.inspect import inspect
    from pyinspect.inspect import Options as inspect_options
    import magicalimport

    def _inspect(target):
        return inspect(
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
                if isclass(member):
                    where = getattr(member, "__module__", None)
                    if where == builtins:
                        continue

                    if all or where == target.__name__:
                        _inspect(member)
                        print("----------------------------------------", file=sys.stdout)
        else:
            print(
                f"sorry {path} is not class (type={type(target)}, repr={target})", file=sys.stderr
            )


if __name__ == "__main__":
    main()
