player_position = 0
computer_position = 0

def board():
    print("•" * (player_position) + "1P" + "•" * (28 - player_position) + "|Goal")
    print("•" * (computer_position) + "COM" + "•" * (27 - computer_position) + "|Goal")

while True:
    board()
    input("Enter를 누르면 말이 움직입니다.")
    player_position += 1
    computer_position += 2
