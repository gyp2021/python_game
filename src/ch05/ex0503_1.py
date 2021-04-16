player_position = 6

def board():
    print("•" * (player_position) + "1P" + "•" * (28 - player_position) + "|Goal")

board()
