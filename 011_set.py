# set() - contains unique elements, unordered, mutable, unindexed

fruits1 = {"apple", "banana", "pear", "watermelon"}
fruits2 = {"pear", "banana", "orange", "apple"}

print(fruits1)  # {'banana', 'pear', 'apple'} # only unicue elements

print(id(fruits1) == id(fruits2))  # False
print(fruits1 == fruits2)  # True

# print(fruits1[0])  # TypeError: 'set' object is not subscriptable

# print(dir(fruits1))
# '__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__',
# '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__',
# '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__',
# '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__',

# 'add',
fruits1.add("kiwi")
print("add: ", fruits1)  # {'banana', 'pear', 'kiwi', 'apple'}

# 'copy',
fruits_copy = fruits1.copy()
print("copy: ", fruits_copy)  # {'banana', 'pear', 'kiwi', 'apple'}

# 'difference',
fruits_difference = fruits1.difference(fruits2)
print("difference: ", fruits_difference)  # {'watermelon', 'kiwi'}

# 'difference_update',
fruits_difference = fruits1.difference_update(fruits2)
print("difference_update: ", fruits_difference)

# 'discard', remove element from set if it exists, do nothing if it doesn't
fruits1.discard("pear")
print("discard: ", fruits1)  # {'banana', 'kiwi', 'apple'}

# 'remove', remove element from set if it exists, raise KeyError if it doesn't
letters = {"a", "b", "c", "d", "e"}
letters.remove("a")

# 'pop',
letters = {"a", "b", "c", "d", "e"}
letters.pop()  # remove and return an ARBITARY! element from the set
print(letters)

# 'union', |
fruits_union = fruits1.union(fruits2)
print("union: ", fruits_union)  # {'banana', 'pear', 'kiwi', 'orange', 'apple'}

# 'intersection', & same items in both sets
fruits_intersection = fruits1.intersection(fruits2)
print("intersection: ", fruits_intersection)  # {'pear', 'banana', 'apple'}

# 'intersection_update',
fruits1.intersection_update(fruits2)
print("intersection_update: ", fruits1)  # {'banana', 'apple'}

# 'issuperset',
fruits1 = {"apple", "banana", "pear"}
fruits2 = {"pear", "banana", "orange", "apple"}
fruits_supeset1 = fruits1.issuperset(fruits2)  # True
fruits_supeset2 = fruits2.issuperset(fruits1)  # False

# 'issubset' - check if all elements of set1 are in set2
fruits1 = {"apple", "banana", "pear", "watermelon"}
fruits2 = {"pear", "banana", "orange", "apple"}
fruits3 = {"kiwi", "mango"}
fruits4 = {"kiwi", "mango", "orange"}
print(fruits1.issubset(fruits2))  # False
print(fruits2.issubset(fruits1))  # False
print(fruits3.issubset(fruits4))  # True
print(fruits4.issubset(fruits3))  # False

# 'isdisjoint',
fruits1 = {"apple", "banana", "pear", "watermelon"}
fruits2 = {"pear", "banana", "orange", "apple"}
fruits3 = {"kiwi", "mango"}
fruits4 = {"kiwi", "mango", "orange"}
print(fruits1.isdisjoint(fruits2))  # False - they have common elements
print(fruits1.isdisjoint(fruits3))  # True - they have no common elements
print(fruits1.isdisjoint(fruits4))  # True - they have no common elements


# 'update'
letters = {"a", "b", "c", "d", "e"}
letters.update({"f", "g", "h"})
print(letters)  # {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}

# 'symmetric_difference', RETURN! a set that contains all items from both sets, except items that are present in both sets:
a = {1, 2, 3, 4, 9}
b = {3, 4, 5, 6, 8}
c1 = a.symmetric_difference(b)  # {1, 2, 5, 6, 8, 9}
c3 = a.union(b) - a.intersection(b)  # {1, 2, 5, 6, 8, 9}
c2 = (a | b) - (a & b)  # {1, 2, 5, 6, 8, 9}
print(a)  # {1, 2, 3, 4, 9}
print(b)  # {3, 4, 5, 6, 8}


# 'symmetric_difference_update', # updates the original set by removing items that are present in both sets, and inserting the other items.
a = {1, 2, 3, 4, 9}
b = {3, 4, 5, 6, 8}
a.symmetric_difference_update(b)
print(a)  # {1, 2, 5, 6, 8, 9}

# 'clear',
fruits1.clear()
print(fruits1)  # set()

# Task! ========================================================================================================================================
a = {1, 2, 3, 4, 9}
b = {3, 4, 5, 6, 8}
a.update({22, 33, 44})
b.update({23, 34, 45})
c = list(a.intersection(b))  # {3, 4}
print(c)  # [3, 4]
