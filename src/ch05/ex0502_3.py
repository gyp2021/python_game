QUESTION = [
    "IU의 본래 이름은?",
    "IU의 아버지 성함은?",
    "IU의 어머니 성함은?",
]
ANSWER = [
    "이지은",
    "이진국",
    "김미삼"
]
ANSWER_ENGLISH = [
    "Lee Ji-eun",
    "Lee",
    "Kim"
]

for i in range(3):
    print(QUESTION[i])
    ans = input()
    if ans == ANSWER[i] or ans == ANSWER_ENGLISH[i]:
        print("You win!")
    else:
        print("You lose!")
