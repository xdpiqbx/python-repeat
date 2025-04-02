# List - is Mutable

fruits1 = ["apple", "banana", "pear", "banana"]
fruits2 = ["pear", "banana", "banana", "apple"]

print(id(fruits1) == id(fruits2))  # False
print(fruits1 == fruits2)  # False

fruits = ["apple", "banana", "pear", "banana"]

# '__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
# '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
# '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',

# 'copy',
fruits_copy = fruits.copy()
print("copy: ", fruits_copy)

# 'count',
cnt = fruits.count("banana")
print("count: ", cnt)

# 'extend',
letters = ["a", "b", "c"]
fruits.extend(letters)
print("extend: ", fruits)


# 'index',
idx = fruits.index("banana")
print("index: ", idx)

# 'insert',
to_index = 2
fruits.insert(to_index, "pineapple")
print("insert: ", fruits)

# 'append',
fruits.append("kiwi")
print("append: ", fruits)

# reverse
fruits.reverse()
print("reverse: ", fruits)

# 'sort'
fruits.sort(reverse=True)
print("sort(reverse=True): ", fruits)

# 'pop',
popped = fruits.pop(0)
print("popped: ", popped)
print("pop: ", fruits)

# 'remove',
fruits.remove("banana")
print("remove: ", fruits)

# clear
fruits.clear()
print("clear: ", fruits)

# ************************************************
hello = "Hello World"
print(list(hello))  # ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

human = {"name": "Bill", "age": "23", "id": 65370}
print(list(human))  # ['name', 'age', 'id']
print(list(human.keys()))  # ['name', 'age', 'id']
print(list(human.values()))  # ['Bill', '23', 65370]

bills = [10, 89, 43, 78, 32, 45]
print(min(bills))
print(max(bills))
print(sum(bills))
print(sum(bills) / len(bills))

ratings = [1, 2, 3, 4, 5, 8]
print(bills + ratings)

# LIST slicing ************************************************

print(bills[:])

# Copy lists ************************************************
new_list_1 = bills[:]
new_list_2 = bills.copy()
new_list_3 = list(bills)
print(id(new_list_1), id(new_list_2), id(new_list_3))
