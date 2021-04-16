import random

ALPABET = ["A", "B", "C", "D", "E", "F", "G"]

rnd = random.choice(ALPABET)
alp = ""

for i in ALPABET:
    if i != rnd:
        alp = alp + i

print(alp)
ans = input("빠진 알파벳은?")

if ans == rnd:
    print("You win!")
else:
    print("You lose!")
