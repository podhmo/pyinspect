# pyinspect

[examples](./examples)

```console
$ pyinspect -h
usage: pyinspect [-h] [--here HERE] {resolve,list,inspect,parse,quote} ...

positional arguments:
  {resolve,list,inspect,parse,quote}

optional arguments:
  -h, --help            show this help message and exit
  --here HERE
```

## resolve

```console
$ pyinspect resolve argparse
/usr/lib/python3.7/argparse.py

$ pyinspect resolve pyinspect | sed "s@$HOME@~@g"
~/venvs/my/pyinspect/pyinspect
```

## list

```console
$ pyinspect list argparse
urllib
urllib.error
urllib.parse
urllib.request
urllib.response
urllib.robotparser

$ pyinspect list pyinspect
pyinspect
pyinspect.cli
pyinspect.code
pyinspect.code.parse
pyinspect.code.quote
pyinspect.inspect
pyinspect.langhelpers
```


## inspect

```console
$ pyinspect inspect collections:Counter
collections:Counter <- builtins:dict <- builtins:object
    [method] __add__(self, other)
    [method] __and__(self, other)
    [method, OVERRIDE] __delitem__(self, elem)
    [method] __iadd__(self, other)
        [method] _keep_positive(self)
    [method] __iand__(self, other)
        [method] _keep_positive(self)
    [method, OVERRIDE] __init__(*args, **kwds)
        [method, OVERRIDE] update(*args, **kwds)
    [method] __ior__(self, other)
        [method] _keep_positive(self)
    [method] __isub__(self, other)
        [method] _keep_positive(self)
    [method] __missing__(self, key)
    [method] __neg__(self)
    [method] __or__(self, other)
    [method] __pos__(self)
    [method, OVERRIDE] __reduce__(self)
    [method, OVERRIDE] __repr__(self)
        [method] most_common(self, n=None)
    [method] __sub__(self, other)
    [method, OVERRIDE] copy(self)
    [method] elements(self)
    [class method, OVERRIDE] fromkeys(iterable, v=None)
    [method] subtract(*args, **kwds)

$ pyinspect inspect pyinspect.code.parse:PyTreeVisitor
pyinspect.code.parse:PyTreeVisitor <- builtins:object
    [method] default_leaf_visit(self, leaf)
    [method] default_node_visit(self, node)
        [method] visit(self, node)
            [method] level
            [method] logger
            [method] default_leaf_visit(self, leaf)
```

## quote

```console
$ pyinspect -f raw quote argparse:L1900
/usr/lib/python3.7/argparse.py
class ArgumentParser(_AttributeHolder, _ActionsContainer):
    """Object for parsing command line strings into Python objects.

    Keyword Arguments:
        - prog -- The name of the program (default: sys.argv[0])
        - usage -- A usage message (default: auto-generated from arguments)
        - description -- A description of what the program does
        - epilog -- Text following the argument descriptions
        - parents -- Parsers whose arguments should be copied into this one
        - formatter_class -- HelpFormatter class for printing help messages
        - prefix_chars -- Characters that prefix optional arguments
        - fromfile_prefix_chars -- Characters that prefix files containing
            additional arguments
        - argument_default -- The default value for all arguments
        - conflict_handler -- String indicating how to handle conflicts
        - add_help -- Add a -h/-help option
        - allow_abbrev -- Allow long options to be abbreviated unambiguously
    """
# ...

    def _parse_known_args(self, arg_strings, namespace):
        # replace arg strings that are file references
        if self.fromfile_prefix_chars is not None:

# ...

        def consume_optional(start_index):

# ...

                    # successfully matched the option; exit the loop
                    elif arg_count == 1:
                        stop = start_index + 1
                        args = [explicit_arg]
                        action_tuples.append((action, args, option_string))
```


## parse

```console
$ pyinspect parse setup.py
  visit_file_input (prefix='', value=None, type=256)
    visit_simple_stmt (prefix='', value=None, type=316)
      visit_import_from (prefix='', value=None, type=300)
        visit_NAME (prefix='', value='from', type=1)
        visit_NAME (prefix=' ', value='setuptools', type=1)
        visit_NAME (prefix=' ', value='import', type=1)
        visit_import_as_names (prefix=' ', value=None, type=299)
          visit_NAME (prefix=' ', value='setup', type=1)
          visit_COMMA (prefix='', value=',', type=12)
          visit_NAME (prefix=' ', value='find_packages', type=1)
      visit_NEWLINE (prefix='', value='\n', type=4)
    visit_simple_stmt (prefix='\n\n', value=None, type=316)
      visit_expr_stmt (prefix='\n\n', value=None, type=290)
        visit_NAME (prefix='\n\n', value='install_requires', type=1)
        visit_EQUAL (prefix=' ', value='=', type=22)
        visit_atom (prefix=' ', value=None, type=266)
          visit_LSQB (prefix=' ', value='[', type=9)
          visit_STRING (prefix='', value='"magicalimport"', type=3)
          visit_RSQB (prefix='', value=']', type=10)
      visit_NEWLINE (prefix='', value='\n', type=4)
    visit_simple_stmt (prefix='', value=None, type=316)
      visit_expr_stmt (prefix='', value=None, type=290)
        visit_NAME (prefix='', value='dev_requires', type=1)
        visit_EQUAL (prefix=' ', value='=', type=22)
        visit_atom (prefix=' ', value=None, type=266)
          visit_LSQB (prefix=' ', value='[', type=9)
          visit_listmaker (prefix='', value=None, type=304)
            visit_STRING (prefix='', value='"black"', type=3)
            visit_COMMA (prefix='', value=',', type=12)
            visit_STRING (prefix=' ', value='"flake8"', type=3)
          visit_RSQB (prefix='', value=']', type=10)
      visit_NEWLINE (prefix='', value='\n', type=4)
    visit_simple_stmt (prefix='', value=None, type=316)
      visit_expr_stmt (prefix='', value=None, type=290)
        visit_NAME (prefix='', value='tests_requires', type=1)
        visit_EQUAL (prefix=' ', value='=', type=22)
        visit_atom (prefix=' ', value=None, type=266)
          visit_LSQB (prefix=' ', value='[', type=9)
          visit_RSQB (prefix='', value=']', type=10)
      visit_NEWLINE (prefix='', value='\n', type=4)
    visit_simple_stmt (prefix='\n', value=None, type=316)
      visit_power (prefix='\n', value=None, type=311)
        visit_NAME (prefix='\n', value='setup', type=1)
        visit_trailer (prefix='', value=None, type=335)
          visit_LPAR (prefix='', value='(', type=7)
          visit_arglist (prefix='\n    ', value=None, type=260)
            visit_argument (prefix='\n    ', value=None, type=261)
              visit_NAME (prefix='\n    ', value='classifiers', type=1)
              visit_EQUAL (prefix='', value='=', type=22)
              visit_atom (prefix='', value=None, type=266)
                visit_LSQB (prefix='', value='[', type=9)
                visit_listmaker (prefix='\n        # "License :: OSI Approved :: MIT License",\n        ', value=None, type=304)
                  visit_STRING (prefix='\n        # "License :: OSI Approved :: MIT License",\n        ', value='"Programming Language :: Python :: 3"', type=3)
                  visit_COMMA (prefix='', value=',', type=12)
                  visit_STRING (prefix='\n        # How mature is this project? Common values are\n        #   3 - Alpha\n        #   4 - Beta\n        #   5 - Production/Stable\n        ', value='"Development Status :: 3 - Alpha"', type=3)
                  visit_COMMA (prefix='', value=',', type=12)
                visit_RSQB (prefix='\n    ', value=']', type=10)
            visit_COMMA (prefix='', value=',', type=12)
            visit_argument (prefix='\n    ', value=None, type=261)
              visit_NAME (prefix='\n    ', value='python_requires', type=1)
              visit_EQUAL (prefix='', value='=', type=22)
              visit_STRING (prefix='', value='">3.5"', type=3)
            visit_COMMA (prefix='', value=',', type=12)
            visit_argument (prefix='\n    ', value=None, type=261)
              visit_NAME (prefix='\n    ', value='packages', type=1)
              visit_EQUAL (prefix='', value='=', type=22)
              visit_power (prefix='', value=None, type=311)
                visit_NAME (prefix='', value='find_packages', type=1)
                visit_trailer (prefix='', value=None, type=335)
                  visit_LPAR (prefix='', value='(', type=7)
                  visit_argument (prefix='', value=None, type=261)
                    visit_NAME (prefix='', value='exclude', type=1)
                    visit_EQUAL (prefix='', value='=', type=22)
                    visit_atom (prefix='', value=None, type=266)
                      visit_LSQB (prefix='', value='[', type=9)
                      visit_STRING (prefix='', value='"pyinspect.tests"', type=3)
                      visit_RSQB (prefix='', value=']', type=10)
                  visit_RPAR (prefix='', value=')', type=8)
            visit_COMMA (prefix='', value=',', type=12)
            visit_argument (prefix='\n    ', value=None, type=261)
              visit_NAME (prefix='\n    ', value='install_requires', type=1)
              visit_EQUAL (prefix='', value='=', type=22)
              visit_NAME (prefix='', value='install_requires', type=1)
            visit_COMMA (prefix='', value=',', type=12)
            visit_argument (prefix='\n    ', value=None, type=261)
              visit_NAME (prefix='\n    ', value='extras_require', type=1)
              visit_EQUAL (prefix='', value='=', type=22)
              visit_atom (prefix='', value=None, type=266)
                visit_LBRACE (prefix='', value='{', type=26)
                visit_dictsetmaker (prefix='', value=None, type=281)
                  visit_STRING (prefix='', value='"testing"', type=3)
                  visit_COLON (prefix='', value=':', type=11)
                  visit_NAME (prefix=' ', value='tests_requires', type=1)
                  visit_COMMA (prefix='', value=',', type=12)
                  visit_STRING (prefix=' ', value='"dev"', type=3)
                  visit_COLON (prefix='', value=':', type=11)
                  visit_NAME (prefix=' ', value='dev_requires', type=1)
                visit_RBRACE (prefix='', value='}', type=27)
            visit_COMMA (prefix='', value=',', type=12)
            visit_argument (prefix='\n    ', value=None, type=261)
              visit_NAME (prefix='\n    ', value='tests_require', type=1)
              visit_EQUAL (prefix='', value='=', type=22)
              visit_NAME (prefix='', value='tests_requires', type=1)
            visit_COMMA (prefix='', value=',', type=12)
            visit_argument (prefix='\n    ', value=None, type=261)
              visit_NAME (prefix='\n    ', value='test_suite', type=1)
              visit_EQUAL (prefix='', value='=', type=22)
              visit_STRING (prefix='', value='"pyinspect.tests"', type=3)
            visit_COMMA (prefix='', value=',', type=12)
          visit_RPAR (prefix='\n', value=')', type=8)
      visit_NEWLINE (prefix='', value='\n', type=4)
    visit_ENDMARKER (prefix='', value='', type=0)
```
