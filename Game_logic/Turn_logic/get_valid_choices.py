from Validations.game_validations import is_occupied
from typing import Sequence

def get_valid_choices(board:Sequence)->list:
    return [str(number) for number in range(1,10) if not is_occupied(board,(number-1))]

