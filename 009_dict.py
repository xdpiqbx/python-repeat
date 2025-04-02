motorbike1 = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2,
}

motorbike2 = {
    'engine_vol': 1.2,
    'price': 25000,
    'brand': 'Ducati',
}

# print(dir(motorbike))
# '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__',
# '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__',
# '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
#

brand = motorbike1['brand']

# dict comparison
print(id(motorbike1) == id(motorbike2))  # False
print(motorbike1 == motorbike2)  # True

# 'copy',
new_moto = motorbike1.copy()
print(new_moto)

# 'fromkeys',
keys = [1, 2, 3, 4]
default = dict.fromkeys(keys)

# 'keys',
motorbike1_keys = list(motorbike1.keys())
print(motorbike1_keys)

# 'values'
motorbike1_values = list(motorbike1.values())
print(motorbike1_values)

# 'get',
price = motorbike1.get('price')
ololo = motorbike1.get('ololo')
atata = motorbike1.get('atata', 'default_value')
print(price)
print(ololo)  # None
print(atata)  # 'default_value'

# 'items',
items = list(motorbike1.items())
print(items)  # [('brand', 'Ducati'), ('price', 25000), ('engine_vol', 1.2)]

# 'popitem', from end of dict
popped_item = motorbike1.popitem()
print(popped_item)  # ('engine_vol', 1.2)
print(motorbike1)  # {'price': 25000}

# 'pop', betterto use pop instead of popitem
popped = motorbike1.pop('brand')
print(popped)  # Ducati
print(motorbike1)  # {'price': 25000, 'engine_vol': 1.2}

# 'setdefault', if key does not exists it will add it with default value
motorbike1.setdefault("color", "black")
print(motorbike1)

# 'update',
motorbike1.update({"tier": "Pirelli Diablo Rosso"})
print(motorbike1)

motorbike1['compression'] = "14:1"
print(motorbike1)

# 'clear',
motorbike1.clear()
print(motorbike1)  # {}
