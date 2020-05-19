'''
Numerical validations.

All functions are boolean.
'''

def is_int(string: str) -> bool:
    '''
    Returns True if the string argument represents a valid integer.
    '''
    try:
        int(string)
    except ValueError:
        return False
    else:
        return True

def is_float(string: str) -> bool:
    '''
    Returns True if the string parameter represents a valid float number.
    '''
    try:
        float(string)
    except ValueError:
        return False
    else:
        return True
