from .string_validations import is_non_empty_string
def is_nonnegative_int_str(int_candidate:str)->bool:
    if not is_non_empty_string(int_candidate):
        return False
    return int_candidate.isdigit()

def is_positive_int_str(int_candidate:str)->bool:
    if not is_nonnegative_int_str(int_candidate):
        return False
    integer = int(int_candidate)
    if not isinstance(integer,int) or isinstance(integer,bool):
        return False
    if not integer > 0:
        return False
    return True


