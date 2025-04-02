fruits = ["apple", "banana", "kiwi", "pear", "orange"]
quantity = [100, 70, 30, 45, 59]
furuits_quantity = zip(fruits, quantity)

print(furuits_quantity)  # <zip object at 0x7f8c4c2b3d00>

print(list(furuits_quantity))
# [('apple', 100), ('banana', 70), ('kiwi', 30), ('pear', 45), ('orange', 59)]

# print(dir(furuits_quantity))
# '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__'


zipped_dict = dict(zip(fruits, quantity))
print(zipped_dict)
# {'apple': 100, 'banana': 70, 'kiwi': 30, 'pear': 45, 'orange': 59}
