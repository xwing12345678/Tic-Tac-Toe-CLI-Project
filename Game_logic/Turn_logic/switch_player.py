from typing import Literal
def switch_active_player(active_player:Literal["x","o"])->Literal["x","o"]:
    if active_player == 'o':
        return 'x'
    return 'o'    