"""Retrieve and print words from a url.

    Usage:
        _type_: _description_
"""
from urllib.request import urlopen

def fetch_words():
    """fetch a list of words from the url

    Args:
        url (_type_): _description_

    Returns:
        _type_: _description_
    """
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_words(words):
    """print the items

    Args:
        items (_type_): _description_
    """
    for word in words:
        print(word)


def main():
    """main call

    Args:
        url (_type_): _description_
    """
    words = fetch_words()
    print_words(words)


if __name__ == '__main__':
    main()
