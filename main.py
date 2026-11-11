from Data.board_data import board_list
from Validations.game_validations import is_occupied
from Game_logic.Turn_logic.get_valid_choices import get_valid_choices
print(get_valid_choices(board_list))
