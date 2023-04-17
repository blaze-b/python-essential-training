c = 5

while c != 0:
    print(c)
    c -= 1

# Augmented assignment
print(c)
c += 10
print(10)
c -= 10
print(c)
c *= 10
print(c)

# Break statement

while True:
    print("Input the number....")
    response = input()
    if int(response) % 7 == 0:
        break
