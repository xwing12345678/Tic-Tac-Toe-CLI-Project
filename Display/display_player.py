from typing import Literal
def display_current_player(player:Literal["x","o"])->str:
    print(f"It is {player}'s turn to move now.")
    return ''