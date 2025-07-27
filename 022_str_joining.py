# Section 31: Соединение строк
# https://www.udemy.com/course/python-ru/learn/lecture/35368786#overview

import datetime

name = 'Bill'
greet = 'Hello ' + 'Python'

# string formatting
f"{greet}. I am {name}"

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")
