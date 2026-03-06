#!/usr/bin/env python3

import alchemy

X = "\033[0m"  # Remove text formatting
D = "\033[2m"  # Dim text formatting

print(f"{D}\nTesting direct module access...{X}")
print("alchemy.elements.create_fire:", alchemy.elements.create_fire())
print("alchemy.elements.create_water:", alchemy.elements.create_water())
print("alchemy.elements.create_earth:", alchemy.elements.create_earth())
print("alchemy.elements.create_air:", alchemy.elements.create_air())

print(f"{D}\nTesting package-level access...{X}")
print("alchemy.create_fire():", alchemy.create_fire())
print("alchemy.create_water():", alchemy.create_water())
try:
    print(alchemy.create_earth())
except AttributeError:
    print("alchemy.create_earth(): AttributeError - function not exposed")
try:
    print(alchemy.create_air())
except AttributeError:
    print("alchemy.create_air(): AttributeError - function not exposed")

print(f"{D}\nPackage metadata{X}\t:", alchemy.__version__)
print(f"{D}Package author{X}\t\t:", alchemy.__author__)
