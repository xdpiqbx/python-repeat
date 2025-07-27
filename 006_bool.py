print(bool(10))  # True
print(bool("abc"))  # True
print(bool([1, 2]))  # True
print(bool(""))  # False
print(bool(None))  # False
print(bool([]))  # False list - []
print(bool({}))  # False dict - {} (empty dict)
print(bool(()))  # False tuple - ()
print(bool(set()))  # False set - {}
print(bool(range(0)))  # False

print(bool(False < True))  # True
