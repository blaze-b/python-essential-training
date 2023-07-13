def display_nth_root(radicand, n):
    root = nth_root(radicand, n)
    message = 'The ' + ordinal(n) + ' root of ' + str(radicand) + " is " + str(root)
    print(message)



def ordinal(value):
    return str(value) + ordinal_suffix(value)


def ordinal_suffix(n):
    s = str(n)
    if s.endswith("11") or s.endswith("12") or s.endswith("13"):
        return 'th'
    if s.endswith("1"):
        return 'st'
    if s.endswith("2"):
        return 'nd'
    if s.endswith("3"):
        return 'rd'
    return 'th'

def nth_root(radicand, n):
    return radicand ** (1/n)


display_nth_root(16, 3)