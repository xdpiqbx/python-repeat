# Range
start = 3
finish = 20
step = 2
result_range = range(start, finish, step)

# print(dir(result_range))  # range(2, 20, 2)
# '__bool__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
#
# 'count',
# 'index',
# 'start',
# 'stop'
# 'step',

print(list(result_range))  # [3, 5, 7, 9, 11, 13, 15, 17, 19]
print(set(result_range))  # [3, 5, 7, 9, 11, 13, 15, 17, 19]
print(tuple(result_range))  # (3, 5, 7, 9, 11, 13, 15, 17, 19)
print(dict.fromkeys(result_range))  # {3: None, 5: None, 7: None, 9: None, ...}

print(result_range.start)
print(result_range.step)
print(result_range.stop)
print(result_range.index(19))  # 8
print(result_range.count(17))  # 1
print(result_range.count(20))  # 0

print(result_range[0])  # 3
print(result_range[1])  # 5
print(result_range[2])  # 7
