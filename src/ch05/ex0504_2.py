import random

ALPABET = ["A", "B", "C", "D", "E", "F", "G"]

rnd = random.choice(ALPABET)
alp = ""

for i in ALPABET:
    if i != rnd:
        alp = alp + i

print(alp)
