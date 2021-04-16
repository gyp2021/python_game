import random
import datetime

ALPABET = ["A", "B", "C", "D", "E", "F", "G"]

rnd = random.choice(ALPABET)
alp = ""

for i in ALPABET:
    if i != rnd:
        alp = alp + i

print(alp)
start = datetime.datetime.now()
ans = input("빠진 알파벳은?")

if ans == rnd:
    print("You win!")
    end = datetime.datetime.now()
    print((end - start))
else:
    print("You lose!")
