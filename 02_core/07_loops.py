c = 5

while c != 0:
    print(c)
    c -= 1

# Break statement

while True:
    print("Input the number....")
    response = input()
    if int(response) % 7 == 0:
        break
