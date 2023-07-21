a = 'Hi I am working, could you please handover the bottle for learning'.split()

print(a)

a.sort(key=len)

print(a)

' '.join(a)

print(a)

# Reversing and copying into copies

x = [4, 9, 2, 1]

y = sorted(x)

# Returns the list

print(y)

p = [9, 3, 1, 0]

q = reversed(p)

print(q)

# Returns the reverse iterator

print(list(q))