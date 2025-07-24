def merge_lists_to_dict(list_1, list_2):
    return dict(zip(list_1, list_2))


l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]

print(merge_lists_to_dict(l1, l2))  # {'a': 1, 'b': 2, 'c': 3}

# Arguments ============================================================
# - positional arguments
# - keyword arguments
# - default arguments
# - variable-length arguments
# - keyword variable-length arguments


def add(*args):
    print(args)  # (1, 2, 3)
    print(type(args))  # <class 'tuple'>
    return sum(args)


print(add(1, 2, 3))  # 6

# ========================= Example of keyword arguments


def add(a, b=100):
    return a + b


add(b=2, a=1)  # 3
add(a=9)  # 109


def get_user_data(**kwargs):
    print(kwargs)  # {'name': 'John', 'age': 30}
    print(type(kwargs))  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")


get_user_data(name="John", age=30)
get_user_data(name="John", age=30, city="New York")
