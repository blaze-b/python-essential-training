t = ("Norway", 48, 5)

print(t)

print(t[0])

print(len(t))

for item in t:
    print(item)

# Can concantenate
t = t + (3333588.10, 265e9)

print(t)


a = ((220, 10), (250, 25), (250, 5454), (250, 788))

print(len(a[2]))
print(a[2] [0], a[2] [1])


h = (391)

print(type(h))

h = (391,)

print(type(h))

h = ()

print(type(h))

p = 1,2,3,2,4

print(type(p))

def min_max(item):
    return min(item), max(item)

values = (78, 88, 45, 34, 35)

print(min_max(values))

# Unpacking

lower, higher = min_max(values)

print(lower, higher)

(a, (b,(c, d))) = (4, (3, (2, 1)))
print(a, b, c, d)

a = 'Jelly'

b = 'Bean'

# swapping
a,b = b,a

print(a, b)

t = tuple([25, 2526, 26, 78])

print(t)

t = tuple("Brian")

print(t)