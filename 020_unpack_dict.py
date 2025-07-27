button = {
    'width': 200,
    'height': 75,
}

button_ok = {
    'text': 'OK!'
}

red_button = {
    **button,
    'color': 'red',
}

print(button)
print(red_button)

pop_up_ok_button = {
    **button_ok,
    **red_button
}
print(pop_up_ok_button)
print(button_ok | red_button)
