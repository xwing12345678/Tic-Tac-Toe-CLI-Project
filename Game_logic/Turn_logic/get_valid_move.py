from Validations.game_validations import is_valid_move
from Validations.number_validations import is_positive_int_str
from Game_logic.Turn_logic.get_valid_choices import get_valid_choices
from Display.display_board import display_board
from typing import Sequence

def get_valid_move(board:Sequence)->str:
    raw_choice = ""
    valid_move:bool = False
    valid_choices = get_valid_choices(board)
    while valid_move == False:
        raw_choice:str = input("Enter the number of the square for your next move! Only enter a number of an unoccupied square! ")
        if not is_positive_int_str(raw_choice):
            print("You did not enter a whole number!")
            display_board(board)
            continue
        if not is_valid_move(valid_choices,raw_choice):
            print("Invalid choice! You must enter the number of an unoccupied square!")
            display_board(board)
            continue
        valid_move = True
        return raw_choice

