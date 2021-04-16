QUESTION = [
    ("IU의 본래 이름은?", "이지은", "Lee Ji-eun"),
    ("IU의 아버지 성함은?", "이진국", "Lee"),
    ("IU의 어머니 성함은?", "김미삼", "Kim")
]

for i in range(3):
    current = QUESTION[i]
    print(current[0])
    ans = input()
    if ans == current[1] or ans == current[2]:
        print("You win!")
    else:
        print("You lose!")
