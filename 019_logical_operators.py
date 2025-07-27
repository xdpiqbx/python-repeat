# Section 28: Логические операторы
# https://www.udemy.com/course/python-ru/learn/lecture/35368760#overview

# not, and, or
res1 = 5-5 or 8-4 or 6-6 or 10-5
print(res1)  # 4

res2 = 10-1 or 8-4 or 6-6 or 10-5
print(res2)  # 9

res3 = 2+2 and 4+1 and "Done"
print(res3)  # Done

res4 = 5+5 and 4-4 and "Done"
print(res4)  # 0
