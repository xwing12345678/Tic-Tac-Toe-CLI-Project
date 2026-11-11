from typing import Literal

def display_result(result_type:Literal["win","draw"],active_player:Literal["x","o"]="x"):
    if result_type == "win":
        print(f'Congratulations {active_player} you have won!!')
    else:
        print("You have run out of empty squares. This game is a draw.")
    print("Thank you for playing with the Tic Tac Toe CLI!")
    return ""  