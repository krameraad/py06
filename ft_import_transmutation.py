#!/usr/bin/env python3

import alchemy
from alchemy.potions import healing_potion as heal
from alchemy import create_water
from alchemy.elements import create_earth, create_fire, strength_potion

X = "\033[0m"
D = "\033[2m"

print(f"{D}\nMethod 1 - Full module import{X}")
print("alchemy.elements.create_fire():", alchemy.elements.create_fire())

print(f"{D}\nMethod 2 - Specific function import{X}")
print("create_water():", create_water())

print(f"{D}\nMethod 3 - Aliased import{X}")
print("heal():", heal())

print(f"{D}\nMethod 4 - Multiple imports{X}")
print("create_earth():", create_earth())
print("create_fire():", create_fire())
print("strength_potion():", strength_potion())
