import random

cnt = 0
while True:
    item = random.randint(1, 100)
    print(item)
    cnt = cnt + 1

    if item == 77:
        break

print(str(cnt) + "번째에 희귀 아이템 겟!")
