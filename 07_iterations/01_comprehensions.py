from math import factorial

words = 'Why sometimes I have believed as many as six impossible things before breakfast'.split()

print(words)

# Comprehensive approach for lists
c1 = [len(word) for word in words]

print(c1)

# Old approach
lengths = []

for word in words:
    lengths.append(len(word))

print(lengths)

f = [len(str(factorial(x))) for x in range(20)]

print(f)

print(type(f))

# Set comprehensions

s = {len(str(factorial(x))) for x in range(20)}

print(type(s))

print(s)
