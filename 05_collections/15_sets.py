p = {14, 25, 26, 47}

print(type(p))


d = {}

print(type(d))

s = set([47, 47, 45, 25, 78, 58, 85, 78, 78])

print(s)


t = [1, 2, 3, 23, 23, 22, 34]

t = set(t)

print(t)


for x in {1, 3, 4, 56, 34}:
    print(x)

q = {2, 9, 6, 4}

print(3 in q)

print(3 not in q)

k = {31, 288}

k.add(23)

print(k)

# Already exiting element with no effect

k.add(288)

k.update([37, 28, 26])

print(k)

# Remove

k.remove(28)

print(k)

k.discard(23)

print(k)

j = k.copy()

j.add(23)

print(k, j)

m = set(j)

print(m)
