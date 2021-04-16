import random
import datetime

ALPABET = [
    "A", "B", "C", "D", "E", "F", "G",
    "H", "I", "J", "K", "L", "M", "N"
    "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"
]

rnd = random.choice(ALPABET)
alp = ""

for i in ALPABET:
    if i != rnd:
        alp = alp + i

print(alp)
start = datetime.datetime.now()

while True:
    ans = input("빠진 알파벳은?")
    if ans == rnd:
        print("You win!")
        end = datetime.datetime.now()
        print((end - start))
        break
    else:
        print("You lose!")
