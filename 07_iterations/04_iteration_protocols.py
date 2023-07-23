iterable = ['Spring', 'Summer', 'Autumn', 'Winter']

iterator = iter(iterable)

print(iterator)

iterable = next(iterator)

print(iterable)

iterable = next(iterator)

print(iterable)

iterable = next(iterator)

print(iterable)


iterable = next(iterator)

print(iterable)

# iterable = next(iterator)

# print(iterable)

# Last will be an excetion with StopIteration


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        return ValueError("iterator is empty")


print(first(['Spring', 'Summer', 'Autumn', 'Winter']))
