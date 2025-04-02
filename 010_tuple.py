# Tuple - IMMUTABILE

fruits1 = ("apple", "banana", "pear", "banana")
fruits2 = ("pear", "banana", "banana", "apple")

print(id(fruits1) == id(fruits2))  # False
print(fruits1 == fruits2)  # False

print(dir(fruits1))
# '__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__',

# 'count',
bananas_count = fruits1.count("banana")
print("count: ", bananas_count)

# 'index'
# banana_index = fruits1.index("banana")
search_from_index = 2
banana_index = fruits1.index("banana", search_from_index)
print("index: ", banana_index)

# ('apple', 'banana', 'pear', 'banana', 'pear', 'banana', 'banana', 'apple')
print(fruits1 + fruits2)

# ('apple', 'banana', 'pear', 'banana', 'apple', 'banana', 'pear', 'banana')
print(fruits1 * 2)

print(fruits1[0])

fruits_list = list(fruits1)  # now you can work with it as with list
print(fruits_list)
fruits_list = tuple(fruits1)  # back to tuple
print(fruits_list)
