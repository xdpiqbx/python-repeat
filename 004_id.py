name1 = "Bill"
name2 = "Bill"
other_name = name1
the_name = name2

# SAME id
print(id(name1))  # 2234240751856
print(id(other_name))  # 2234240751856
print(id(name2))  # 2234240751856
print(id(the_name))  # 2234240751856


class Human:
    name: None
    age: None


bill1 = Human()
bill2 = Human()

bill1.name = "Bill"
bill1.age = "10"

bill2.name = "Bill"
bill2.age = "10"

# Different! id
print(id(bill1))  # 1898429513504
print(id(bill2))  # 1898429513456
