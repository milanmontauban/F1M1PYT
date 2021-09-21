microbit_milan
from microbit import *

dog = Image("00000:09000:99000:09990:09090")

display.scroll('HELLO YOU!')

while True:
    if button_a.is_pressed():
        display.scroll('Ik ben Joeri')
    elif button_b.is_pressed():
        display.show(dog)

display.clear()