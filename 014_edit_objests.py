num_1 = 8
num_2 = 8
num_3 = 8

# They all have the same value, and they are the same object in memory.
# because the are immutable objects
print(id(num_1))  # 140726769012064
print(id(num_2))  # 140726769012064
print(id(num_3))  # 140726769012064

# ----------------------------------------------------------------------------
nums_1 = [1, 2, 3, 4, 5]
nums_2 = [1, 2, 3, 4, 5]
nums_3 = [1, 2, 3, 4, 5]

# They all have the same values, but they are different objects in memory.
# because the are mutable objects
print(id(nums_1))  # 2022719674624
print(id(nums_2))  # 2022719672704
print(id(nums_3))  # 2022722582144

# So, how to prevent editing of mutable objects?
# 1. Use immutable objects like tuples instead of lists.
# 2. Use copy() method to create a shallow copy of the list.
# 3. Use deepcopy() method from the copy module to create a deep copy of the list.
# 4. Use frozenset() to create an immutable set.
# 5. Use namedtuple() from the collections module to create an immutable tuple.
# 6. Use dataclasses from the dataclasses module to create immutable classes.
# 7. Use the @property decorator to create read-only properties in classes.

# copy()

# from copy import deepcopy
# deepcopy()
