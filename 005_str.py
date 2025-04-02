name = "Bill"

print(type(name))  # <class 'str'>

print(dir(name))
# '__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',

#
# 'casefold', 'lower', 'upper', 'capitalize', 'title',
# 'join', 'split',
# 'center',
# 'count',
# 'encode',
# 'endswith',
# 'expandtabs',
# 'find',
# 'format',
# 'format_map',
# 'index',
# 'isalnum',
# 'isalpha',
# 'isascii',
# 'isdecimal',
# 'isdigit',
# 'isidentifier',
# 'islower',
# 'isnumeric',
# 'isprintable',
# 'isspace',
# 'istitle',
# 'isupper',
# 'ljust',
# 'lstrip',
# 'maketrans',
# 'partition',
# 'removeprefix',
# 'removesuffix',

# 'replace',
# 'rfind',
# 'rindex',
# 'rjust',
# 'rpartition',
# 'rsplit',
# 'rstrip',

# 'splitlines',
# 'startswith',
# 'strip',
# 'swapcase',
# 'translate',
# 'zfill'


print(name.__len__())
print(len(name))
print(name[1:])
print(name[::-1])  # lliB [from:to:step]
