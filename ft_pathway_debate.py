#!/usr/bin/env python3

import alchemy.transmutation
from alchemy.transmutation import \
    lead_to_gold, stone_to_gem, \
    philosophers_stone, elixir_of_life

X = "\033[0m"
D = "\033[2m"
H = "\033[1m"

print(f"{H}=== Pathway Debate Mastery ==={X}")
print(f"{D}\nTesting absolute imports (from basic.py):{X}")
print("lead_to_gold(): " + lead_to_gold())
print("lead_to_gold(): " + stone_to_gem())

print(f"{D}\nTesting relative imports (from advanced.py):{X}")
print("philosophers_stone(): " + philosophers_stone())
print("elixir_of_life(): " + elixir_of_life())

print(f"{D}\nTesting package access:{X}")
print("alchemy.transmutation.lead_to_gold(): "
      + alchemy.transmutation.lead_to_gold())
print("alchemy.transmutation.philosophers_stone(): "
      + alchemy.transmutation.philosophers_stone())

print(f"{H}\nBoth pathways work! Absolute: clear, Relative: concise{X}")
