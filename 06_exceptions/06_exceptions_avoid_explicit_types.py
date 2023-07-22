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
    if not isinstance(s, list):
        raise TypeError("Arquement must be a list")
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


def main():
    convert("one two three".split())
    convert(457)


if __name__ == '__main__':
    main()
