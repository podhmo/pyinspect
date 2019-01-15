```
pyinspect inspect -n collections
00:collections:deque <- builtins:object
01:    [method] __add__(self, value, /)
01:    [method] __bool__(self, /)
01:    [method] __contains__(self, key, /)
01:    [method] __copy__
01:    [method] __delitem__(self, key, /)
01:    [method, OVERRIDE] __eq__(self, value, /)
01:    [method, OVERRIDE] __ge__(self, value, /)
01:    [method, OVERRIDE] __getattribute__(self, name, /)
01:    [method] __getitem__(self, key, /)
01:    [method, OVERRIDE] __gt__(self, value, /)
01:    [method] __iadd__(self, value, /)
01:    [method] __imul__(self, value, /)
01:    [method, OVERRIDE] __init__(self, /, *args, **kwargs)
01:    [method] __iter__(self, /)
01:    [method, OVERRIDE] __le__(self, value, /)
01:    [method] __len__(self, /)
01:    [method, OVERRIDE] __lt__(self, value, /)
01:    [method] __mul__(self, value, /)
01:    [method, OVERRIDE] __ne__(self, value, /)
01:    [static method, OVERRIDE] __new__(*args, **kwargs)
01:    [method, OVERRIDE] __reduce__
01:    [method, OVERRIDE] __repr__(self, /)
01:    [method] __reversed__
01:    [method] __rmul__(self, value, /)
01:    [method] __setitem__(self, key, value, /)
01:    [method, OVERRIDE] __sizeof__
01:    [method] append
01:    [method] appendleft
01:    [method] clear
01:    [method] copy
01:    [method] count
01:    [method] extend
01:    [method] extendleft
01:    [method] index
01:    [method] insert
01:    [method] pop
01:    [method] popleft
01:    [method] remove
01:    [method] reverse
01:    [method] rotate

----------------------------------------
00:collections:defaultdict <- builtins:dict <- builtins:object
01:    [method] __copy__
01:    [method, OVERRIDE] __getattribute__(self, name, /)
01:    [method, OVERRIDE] __init__(self, /, *args, **kwargs)
01:    [method] __missing__
01:    [method, OVERRIDE] __reduce__
01:    [method, OVERRIDE] __repr__(self, /)
01:    [method, OVERRIDE] copy

----------------------------------------
00:collections:_OrderedDictKeysView <- collections.abc:KeysView <- collections.abc:MappingView <- collections.abc:Set <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method] __reversed__(self)

00:collections.abc:KeysView <- collections.abc:MappingView <- collections.abc:Set <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method, OVERRIDE] __contains__(self, key)
01:    [method, OVERRIDE] __iter__(self)
01:    [class method, OVERRIDE] _from_iterable(it)

00:collections.abc:MappingView <- collections.abc:Sized <- builtins:object
01:    [method, OVERRIDE] __init__(self, mapping)
01:    [method, OVERRIDE] __len__(self)
01:    [method, OVERRIDE] __repr__(self)

00:collections.abc:Set <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method] __and__(self, other)
02:        [class method] _from_iterable(it)
01:    [method, OVERRIDE] __eq__(self, other)
02:        [method, OVERRIDE] __le__(self, other)
01:    [method, OVERRIDE] __gt__(self, other)
02:        [method, OVERRIDE] __ge__(self, other)
01:    [method, OVERRIDE] __lt__(self, other)
02:        [method, OVERRIDE] __le__(self, other)
01:    [method] __or__(self, other)
02:        [class method] _from_iterable(it)
01:    [method] __rand__(self, other)
02:        [class method] _from_iterable(it)
01:    [method] __ror__(self, other)
02:        [class method] _from_iterable(it)
01:    [method] __rsub__(self, other)
02:        [class method] _from_iterable(it)
01:    [method] __rxor__(self, other)
02:        [class method] _from_iterable(it)
01:    [method] __sub__(self, other)
02:        [class method] _from_iterable(it)
01:    [method] __xor__(self, other)
02:        [class method] _from_iterable(it)
01:    [method] _hash(self)
01:    [method] isdisjoint(self, other)

00:collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Sized <- builtins:object
01:    [method] __len__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Iterable <- builtins:object
01:    [method] __iter__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Container <- builtins:object
01:    [method] __contains__(self, x)
01:    [class method, OVERRIDE] __subclasshook__(C)

----------------------------------------
00:collections:_OrderedDictItemsView <- collections.abc:ItemsView <- collections.abc:MappingView <- collections.abc:Set <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method] __reversed__(self)

00:collections.abc:ItemsView <- collections.abc:MappingView <- collections.abc:Set <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method, OVERRIDE] __contains__(self, item)
01:    [method, OVERRIDE] __iter__(self)
01:    [class method, OVERRIDE] _from_iterable(it)

00:collections.abc:MappingView <- collections.abc:Sized <- builtins:object
01:    [method, OVERRIDE] __init__(self, mapping)
01:    [method, OVERRIDE] __len__(self)
01:    [method, OVERRIDE] __repr__(self)

00:collections.abc:Set <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method] __and__(self, other)
02:        [class method] _from_iterable(it)
01:    [method, OVERRIDE] __eq__(self, other)
02:        [method, OVERRIDE] __le__(self, other)
01:    [method, OVERRIDE] __gt__(self, other)
02:        [method, OVERRIDE] __ge__(self, other)
01:    [method, OVERRIDE] __lt__(self, other)
02:        [method, OVERRIDE] __le__(self, other)
01:    [method] __or__(self, other)
02:        [class method] _from_iterable(it)
01:    [method] __rand__(self, other)
02:        [class method] _from_iterable(it)
01:    [method] __ror__(self, other)
02:        [class method] _from_iterable(it)
01:    [method] __rsub__(self, other)
02:        [class method] _from_iterable(it)
01:    [method] __rxor__(self, other)
02:        [class method] _from_iterable(it)
01:    [method] __sub__(self, other)
02:        [class method] _from_iterable(it)
01:    [method] __xor__(self, other)
02:        [class method] _from_iterable(it)
01:    [method] _hash(self)
01:    [method] isdisjoint(self, other)

00:collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Sized <- builtins:object
01:    [method] __len__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Iterable <- builtins:object
01:    [method] __iter__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Container <- builtins:object
01:    [method] __contains__(self, x)
01:    [class method, OVERRIDE] __subclasshook__(C)

----------------------------------------
00:collections:_OrderedDictValuesView <- collections.abc:ValuesView <- collections.abc:MappingView <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method] __reversed__(self)

00:collections.abc:ValuesView <- collections.abc:MappingView <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method, OVERRIDE] __contains__(self, value)
01:    [method, OVERRIDE] __iter__(self)

00:collections.abc:MappingView <- collections.abc:Sized <- builtins:object
01:    [method, OVERRIDE] __init__(self, mapping)
01:    [method, OVERRIDE] __len__(self)
01:    [method, OVERRIDE] __repr__(self)

00:collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Sized <- builtins:object
01:    [method] __len__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Iterable <- builtins:object
01:    [method] __iter__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Container <- builtins:object
01:    [method] __contains__(self, x)
01:    [class method, OVERRIDE] __subclasshook__(C)

----------------------------------------
00:collections:_Link <- builtins:object

----------------------------------------
00:collections:OrderedDict <- builtins:dict <- builtins:object
01:    [method, OVERRIDE] __delitem__(self, key, /)
01:    [method, OVERRIDE] __eq__(self, value, /)
01:    [method, OVERRIDE] __ge__(self, value, /)
01:    [method, OVERRIDE] __gt__(self, value, /)
01:    [method, OVERRIDE] __init__(self, /, *args, **kwargs)
01:    [method, OVERRIDE] __iter__(self, /)
01:    [method, OVERRIDE] __le__(self, value, /)
01:    [method, OVERRIDE] __lt__(self, value, /)
01:    [method, OVERRIDE] __ne__(self, value, /)
01:    [static method, OVERRIDE] __new__(*args, **kwargs)
01:    [method, OVERRIDE] __reduce__
01:    [method, OVERRIDE] __repr__(self, /)
01:    [method] __reversed__
01:    [method, OVERRIDE] __setitem__(self, key, value, /)
01:    [method, OVERRIDE] __sizeof__
01:    [method, OVERRIDE] clear
01:    [method, OVERRIDE] copy
01:    [class method, OVERRIDE] fromkeys(iterable, value=None)
01:    [method, OVERRIDE] items
01:    [method, OVERRIDE] keys
01:    [method] move_to_end(self, /, key, last=True)
01:    [method, OVERRIDE] pop
01:    [method, OVERRIDE] popitem(self, /, last=True)
01:    [method, OVERRIDE] setdefault(self, /, key, default=None)
01:    [method, OVERRIDE] update
01:    [method, OVERRIDE] values

----------------------------------------
00:[function] namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
01:    [function] OrderedDict
----------------------------------------
00:collections:Counter <- builtins:dict <- builtins:object
01:    [method] __add__(self, other)
01:    [method] __and__(self, other)
01:    [method, OVERRIDE] __delitem__(self, elem)
01:    [method] __iadd__(self, other)
02:        [method] _keep_positive(self)
01:    [method] __iand__(self, other)
02:        [method] _keep_positive(self)
01:    [method, OVERRIDE] __init__(*args, **kwds)
02:        [method, OVERRIDE] update(*args, **kwds)
01:    [method] __ior__(self, other)
02:        [method] _keep_positive(self)
01:    [method] __isub__(self, other)
02:        [method] _keep_positive(self)
01:    [method] __missing__(self, key)
01:    [method] __neg__(self)
01:    [method] __or__(self, other)
01:    [method] __pos__(self)
01:    [method, OVERRIDE] __reduce__(self)
01:    [method, OVERRIDE] __repr__(self)
02:        [method] most_common(self, n=None)
01:    [method] __sub__(self, other)
01:    [method, OVERRIDE] copy(self)
01:    [method] elements(self)
01:    [class method, OVERRIDE] fromkeys(iterable, v=None)
01:    [method] subtract(*args, **kwds)

----------------------------------------
00:collections:ChainMap <- collections.abc:MutableMapping <- collections.abc:Mapping <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method] __bool__(self)
01:    [method, OVERRIDE] __contains__(self, key)
01:    [method] __copy__(self)
01:    [method, OVERRIDE] __delitem__(self, key)
01:    [method, OVERRIDE] __getitem__(self, key)
02:        [method] __missing__(self, key)
01:    [method, OVERRIDE] __init__(self, *maps)
01:    [method, OVERRIDE] __iter__(self)
01:    [method, OVERRIDE] __len__(self)
01:    [method, OVERRIDE] __repr__(self)
01:    [method, OVERRIDE] __setitem__(self, key, value)
01:    [method, OVERRIDE] clear(self)
01:    [method] copy(self)
01:    [class method] fromkeys(iterable, *args)
01:    [method, OVERRIDE] get(self, key, default=None)
01:    [method] new_child(self, m=None)
01:    [property] parents
01:    [method, OVERRIDE] pop(self, key, *args)
01:    [method, OVERRIDE] popitem(self)

00:collections.abc:MutableMapping <- collections.abc:Mapping <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method] __delitem__(self, key)
01:    [method] __setitem__(self, key, value)
01:    [method] clear(self)
02:        [method] popitem(self)
01:    [method] pop(self, key, default=<object object at 0x7f5037e9a070>)
01:    [method] setdefault(self, key, default=None)
01:    [method] update(*args, **kwds)

00:collections.abc:Mapping <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method, OVERRIDE] __contains__(self, key)
01:    [method, OVERRIDE] __eq__(self, other)
02:        [method] items(self)
01:    [method] __getitem__(self, key)
01:    [method] get(self, key, default=None)
01:    [method] keys(self)
01:    [method] values(self)

00:collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Sized <- builtins:object
01:    [method] __len__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Iterable <- builtins:object
01:    [method] __iter__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Container <- builtins:object
01:    [method] __contains__(self, x)
01:    [class method, OVERRIDE] __subclasshook__(C)

----------------------------------------
00:collections:UserDict <- collections.abc:MutableMapping <- collections.abc:Mapping <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method, OVERRIDE] __contains__(self, key)
01:    [method, OVERRIDE] __delitem__(self, key)
01:    [method, OVERRIDE] __getitem__(self, key)
01:    [method, OVERRIDE] __init__(*args, **kwargs)
01:    [method, OVERRIDE] __iter__(self)
01:    [method, OVERRIDE] __len__(self)
01:    [method, OVERRIDE] __repr__(self)
01:    [method, OVERRIDE] __setitem__(self, key, item)
01:    [method] copy(self)
01:    [class method] fromkeys(iterable, value=None)

00:collections.abc:MutableMapping <- collections.abc:Mapping <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method] __delitem__(self, key)
01:    [method] __setitem__(self, key, value)
01:    [method] clear(self)
02:        [method] popitem(self)
01:    [method] pop(self, key, default=<object object at 0x7f5037e9a070>)
01:    [method] setdefault(self, key, default=None)
01:    [method] update(*args, **kwds)

00:collections.abc:Mapping <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method, OVERRIDE] __contains__(self, key)
01:    [method, OVERRIDE] __eq__(self, other)
02:        [method] items(self)
01:    [method] __getitem__(self, key)
01:    [method] get(self, key, default=None)
01:    [method] keys(self)
01:    [method] values(self)

00:collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Sized <- builtins:object
01:    [method] __len__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Iterable <- builtins:object
01:    [method] __iter__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Container <- builtins:object
01:    [method] __contains__(self, x)
01:    [class method, OVERRIDE] __subclasshook__(C)

----------------------------------------
00:collections:UserList <- collections.abc:MutableSequence <- collections.abc:Sequence <- collections.abc:Reversible <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method] _UserList__cast(self, other)
01:    [method] __add__(self, other)
01:    [method, OVERRIDE] __contains__(self, item)
01:    [method, OVERRIDE] __delitem__(self, i)
01:    [method, OVERRIDE] __eq__(self, other)
01:    [method, OVERRIDE] __ge__(self, other)
01:    [method, OVERRIDE] __getitem__(self, i)
01:    [method, OVERRIDE] __gt__(self, other)
01:    [method, OVERRIDE] __iadd__(self, other)
01:    [method] __imul__(self, n)
01:    [method, OVERRIDE] __init__(self, initlist=None)
01:    [method, OVERRIDE] __le__(self, other)
01:    [method, OVERRIDE] __len__(self)
01:    [method, OVERRIDE] __lt__(self, other)
01:    [method] __mul__(self, n)
01:    [method] __radd__(self, other)
01:    [method, OVERRIDE] __repr__(self)
01:    [method] __rmul__(self, n)
01:    [method, OVERRIDE] __setitem__(self, i, item)
01:    [method, OVERRIDE] append(self, item)
01:    [method, OVERRIDE] clear(self)
01:    [method] copy(self)
01:    [method, OVERRIDE] count(self, item)
01:    [method, OVERRIDE] extend(self, other)
01:    [method, OVERRIDE] index(self, item, *args)
01:    [method, OVERRIDE] insert(self, i, item)
01:    [method, OVERRIDE] pop(self, i=-1)
01:    [method, OVERRIDE] remove(self, item)
01:    [method, OVERRIDE] reverse(self)
01:    [method] sort(self, *args, **kwds)

00:collections.abc:MutableSequence <- collections.abc:Sequence <- collections.abc:Reversible <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method] __delitem__(self, index)
01:    [method] __iadd__(self, values)
02:        [method] extend(self, values)
03:            [method] append(self, value)
04:                [method] insert(self, index, value)
01:    [method] __setitem__(self, index, value)
01:    [method] clear(self)
02:        [method] pop(self, index=-1)
01:    [method] remove(self, value)
01:    [method] reverse(self)

00:collections.abc:Sequence <- collections.abc:Reversible <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method, OVERRIDE] __contains__(self, value)
01:    [method] __getitem__(self, index)
01:    [method, OVERRIDE] __iter__(self)
01:    [method, OVERRIDE] __reversed__(self)
01:    [method] count(self, value)
01:    [method] index(self, value, start=0, stop=None)

00:collections.abc:Reversible <- collections.abc:Iterable <- builtins:object
01:    [method] __reversed__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Sized <- builtins:object
01:    [method] __len__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Iterable <- builtins:object
01:    [method] __iter__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Container <- builtins:object
01:    [method] __contains__(self, x)
01:    [class method, OVERRIDE] __subclasshook__(C)

----------------------------------------
00:collections:UserString <- collections.abc:Sequence <- collections.abc:Reversible <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method] __add__(self, other)
01:    [method] __complex__(self)
01:    [method, OVERRIDE] __contains__(self, char)
01:    [method, OVERRIDE] __eq__(self, string)
01:    [method] __float__(self)
01:    [method, OVERRIDE] __ge__(self, string)
01:    [method, OVERRIDE] __getitem__(self, index)
01:    [method] __getnewargs__(self)
01:    [method, OVERRIDE] __gt__(self, string)
01:    [method, OVERRIDE] __hash__(self)
01:    [method, OVERRIDE] __init__(self, seq)
01:    [method] __int__(self)
01:    [method, OVERRIDE] __le__(self, string)
01:    [method, OVERRIDE] __len__(self)
01:    [method, OVERRIDE] __lt__(self, string)
01:    [method] __mod__(self, args)
01:    [method] __mul__(self, n)
01:    [method] __radd__(self, other)
01:    [method, OVERRIDE] __repr__(self)
01:    [method] __rmod__(self, format)
01:    [method] __rmul__(self, n)
01:    [method, OVERRIDE] __str__(self)
01:    [method] capitalize(self)
01:    [method] casefold(self)
01:    [method] center(self, width, *args)
01:    [method, OVERRIDE] count(self, sub, start=0, end=9223372036854775807)
01:    [method] encode(self, encoding=None, errors=None)
01:    [method] endswith(self, suffix, start=0, end=9223372036854775807)
01:    [method] expandtabs(self, tabsize=8)
01:    [method] find(self, sub, start=0, end=9223372036854775807)
01:    [method] format(self, *args, **kwds)
01:    [method] format_map(self, mapping)
01:    [method, OVERRIDE] index(self, sub, start=0, end=9223372036854775807)
01:    [method] isalnum(self)
01:    [method] isalpha(self)
01:    [method] isascii(self)
01:    [method] isdecimal(self)
01:    [method] isdigit(self)
01:    [method] isidentifier(self)
01:    [method] islower(self)
01:    [method] isnumeric(self)
01:    [method] isprintable(self)
01:    [method] isspace(self)
01:    [method] istitle(self)
01:    [method] isupper(self)
01:    [method] join(self, seq)
01:    [method] ljust(self, width, *args)
01:    [method] lower(self)
01:    [method] lstrip(self, chars=None)
01:    [static method] maketrans(x, y=None, z=None, /)
01:    [method] partition(self, sep)
01:    [method] replace(self, old, new, maxsplit=-1)
01:    [method] rfind(self, sub, start=0, end=9223372036854775807)
01:    [method] rindex(self, sub, start=0, end=9223372036854775807)
01:    [method] rjust(self, width, *args)
01:    [method] rpartition(self, sep)
01:    [method] rsplit(self, sep=None, maxsplit=-1)
01:    [method] rstrip(self, chars=None)
01:    [method] split(self, sep=None, maxsplit=-1)
01:    [method] splitlines(self, keepends=False)
01:    [method] startswith(self, prefix, start=0, end=9223372036854775807)
01:    [method] strip(self, chars=None)
01:    [method] swapcase(self)
01:    [method] title(self)
01:    [method] translate(self, *args)
01:    [method] upper(self)
01:    [method] zfill(self, width)

00:collections.abc:Sequence <- collections.abc:Reversible <- collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [method, OVERRIDE] __contains__(self, value)
01:    [method] __getitem__(self, index)
01:    [method, OVERRIDE] __iter__(self)
01:    [method, OVERRIDE] __reversed__(self)
01:    [method] count(self, value)
01:    [method] index(self, value, start=0, stop=None)

00:collections.abc:Reversible <- collections.abc:Iterable <- builtins:object
01:    [method] __reversed__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Collection <- collections.abc:Sized <- collections.abc:Iterable <- collections.abc:Container <- builtins:object
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Sized <- builtins:object
01:    [method] __len__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Iterable <- builtins:object
01:    [method] __iter__(self)
01:    [class method, OVERRIDE] __subclasshook__(C)

00:collections.abc:Container <- builtins:object
01:    [method] __contains__(self, x)
01:    [class method, OVERRIDE] __subclasshook__(C)

----------------------------------------
```
