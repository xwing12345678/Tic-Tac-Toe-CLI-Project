from typing import Literal
from Game_logic.Turn_logic.switch_player import switch_active_player

def change_square(board:list,player:Literal["x","o"],square:str):
    board[int(square)-1] = player