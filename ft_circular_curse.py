#!/usr/bin/env python3

from alchemy.grimoire import record_spell, validate_ingredients

X = "\033[0m"  # Remove text formatting
D = "\033[2m"  # Dim text formatting
H = "\033[1m"  # Header text formatting

print(f"{H}\n=== Circular Curse Breaking ==={X}")

print(f"{D}\nTesting ingredient validation:{X}")
print("validate_ingredients('fire air'):",
      validate_ingredients('fire air'))
print("validate_ingredients('dragon scales'):",
      validate_ingredients('dragon scales'))

print(f"{D}\nTesting spell recording with validation:{X}")
print("record_spell('Fireball', 'fire air'):",
      record_spell('Fireball', 'fire air'))
print("record_spell('Dark Magic', 'shadow'):",
      record_spell('Dark Magic', 'shadow'))

print(f"{D}\nTesting late import technique:{X}")
print("record_spell('Lightning', 'air'):",
      record_spell('Lightning', 'air'))

print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely.")
