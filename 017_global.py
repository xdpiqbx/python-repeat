# 108 Ключевое слово global в функциях
# 109 Практика - Глобальные и локальные переменные

a = 10


def myFn():
    b = 4
    c = 8
    global a
    a = 15
    print(dir())  # ['b', 'c']


myFn()
print(a)  # 15

print(dir())
# [..., '__spec__', 'a', 'myFn']
