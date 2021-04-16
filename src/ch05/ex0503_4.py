import random

# plyaer_name = "1P"
# computer_name = "COM"

# player_name_length = plyaer_name.len() # 2
# computer_name_length = computer_name.len() # 3

# total_line_length = 30
# player_line_length = total_line_length - player_name_length
# computer_line_length = total_line_length - computer_name_length

player_position = 0
computer_position = 0

def board():
    print("•" * (player_position) + "P" + "•" * (29 - player_position) + "|Goal")
    print("•" * (computer_position) + "C" + "•" * (29 - computer_position) + "|Goal")

board()
print("START!")

while True:
    input("Enter를 누르면 말이 움직입니다. 1P")
    player_position = player_position + random.randint(1, 6)
    if player_position > 29:
        player_position = 29
    board()
    if player_position == 29:
        print("You win!")
        break

    input("Enter를 누르면 말이 움직입니다. COM")
    computer_position = computer_position + random.randint(1, 6)
    if computer_position > 29:
        computer_position = 29
    board()
    if computer_position == 29:
        print("You lose!")
        break
