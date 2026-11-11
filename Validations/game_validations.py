from typing import Sequence
from Validations.number_validations import is_positive_int_str
from Validations.string_validations import is_non_empty_string

def is_occupied(board:Sequence, choice:int)->bool:
     if board[choice]:
          return True
     return False

def in_valid_choices(valid_choices:Sequence[str], choice:str)->bool:
    return choice in valid_choices


def is_valid_move(valid_choices:Sequence[str], choice:str)->bool:
     if not is_positive_int_str(choice):
          return False
     if not in_valid_choices(valid_choices,choice):
          return False
     return True


     
     


