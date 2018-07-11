import sys


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("target_list", nargs="+")
    args = parser.parse_args(argv)
    run(**vars(args))


def run(*, target_list):
    from inspect import isclass
    from pyinspect.inspect import inspect
    import magicalimport

    for path in target_list:
        target = magicalimport.import_symbol(path)
        if isclass(target):
            inspect.inspect(target)
        else:
            print(f"sorry {path} is not class (type={type(target)}, repr={target})", file=sys.stderr)


if __name__ == "__main__":
    main()
