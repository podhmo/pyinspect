def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("target_list", nargs="+")
    args = parser.parse_args(argv)
    run(**vars(args))


def run(*, target_list):
    from pyinspect import inspect
    import magicalimport

    for path in target_list:
        target = magicalimport.import_symbol(path)
        inspect.inspect(target)


if __name__ == "__main__":
    main()
