# sec 30 del
# https://www.udemy.com/course/python-ru/learn/lecture/35368782#overview

motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2,
}

del motorbike['brand']
motorbike.__delitem__('price')

print(motorbike)
