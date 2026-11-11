from typing import Literal
from Data.board_data import board_list
from Game_logic.Turn_logic.switch_player import switch_active_player
from Game_logic.Victory_Logic.is_draw import is_draw
from Game_logic.Turn_logic.turn_flow import turn_flow
from Game_logic.Victory_Logic.is_victory import is_victory
from Display.display_result import display_result

def main(board):
    playing = True
    player:Literal['x','o'] = 'x'
    while playing:
        turn_flow(board,player)
        if is_victory(board_list,player):
            display_result('win',player)
            playing = False
            break

        elif is_draw(board_list):
            display_result('draw')
            playing = False
            break
        else:
            player = switch_active_player(player)

main(board_list)


            
        
        
        


        

