from math import log
import sys

DIGIT_MP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def convert(s):
    """Convert a string to an integer"""
    try:
        number = ''
        for token in s:
            number += DIGIT_MP[token]
        x = int(number)
        print(f'Converted successfully! x = {x}')
        return x
    except (KeyError, TypeError) as e:
        print(f'Conversion error: {e!r}', file=sys.stderr)
        raise


def string_log(s):
    v = convert(s)
    return log(v)
