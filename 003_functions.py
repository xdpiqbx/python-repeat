def hello(name, age=5):
    print(f"Hello! {name}")
    return age


hello("Bill")
print(hello("Bill", 15))

# Function will return None if you do not use "return" keyword
# print() always return None
