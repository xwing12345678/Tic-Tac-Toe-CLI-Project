from typing import Sequence
from Game_logic.Turn_logic.get_valid_choices import get_valid_choices

def is_draw(board:Sequence)->bool:
    empty_square_list = get_valid_choices(board)
    if empty_square_list:
        return False
    return True
    

