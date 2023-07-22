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
    number = ''
    for token in s:
        number += DIGIT_MP[token]
    x = int(number)
    return x


def convert_1(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MP[token]
        x = int(number)
        print(f'Converted successfully! x = {x}')
    except KeyError:
        print('Convertion failed....')
        x = -1
    except TypeError:
        print('Convertion failed....')
        x = -1
    return x


def convert_2(s):
    """Convert a string to an integer"""
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MP[token]
        x = int(number)
        print(f'Converted successfully! x = {x}')
    except (KeyError, TypeError):
        print('Convertion failed....')
    return x


def convert_3(s):
    """Convert a string to an integer"""
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MP[token]
        x = int(number)
        print(f'Converted successfully! x = {x}')
    except (KeyError, TypeError):
        pass
    return x


def convert_4(s):
    """Convert a string to an integer"""
    try:
        number = ''
        for token in s:
            number += DIGIT_MP[token]
        x = int(number)
        print(f'Converted successfully! x = {x}')
        return x
    except (KeyError, TypeError):
        print('Convertion failed....')
        return -1


def convert_5(s):
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
        return -1
