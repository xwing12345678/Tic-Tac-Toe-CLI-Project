from typing import Literal
from .get_valid_move import get_valid_move
from Display.display_board import display_board
from .switch_player import switch_active_player
from Display.display_player import display_current_player
from Display.display_result import display_result
from Data.change_square import change_square


def turn_flow(board,player:Literal["x","o"]):
    display_board(board)
    display_current_player(player)
    valid_move = get_valid_move(board)
    change_square(board,player,valid_move)





    
    


