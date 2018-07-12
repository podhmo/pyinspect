import sys


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("target_list", nargs="+")
    parser.add_argument("--only-this", action="store_true")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("-n", "--show-level", action="store_true")
    parser.add_argument("--skip-special-method", action="store_true", help="skip __foo__()")
    parser.add_argument("--skip-private-method", action="store_true", help="skip _foo()")
    args = parser.parse_args(argv)
    run(**vars(args))


def run(
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
        if ":" in path:
            target = magicalimport.import_symbol(path, sep=":")
        else:
            target = magicalimport.import_module(path)

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
