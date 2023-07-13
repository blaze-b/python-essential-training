if True:
    print("It's true!")
if False:
    print("It's true!")
if bool("eggs"):
    print("Yes Please!")
if "eggs":
    print("Yes Please!")

# Else Block

h = 42
if h > 50:
    print("Greater than 50")
else:
    print("50 or smaller")

if h > 50:
    print("Greater than 50")
else:
    if h < 20:
        print("Less than 20")
    else:
        print("Between 20 and 50")

if h > 50:
    print("Greater than 50")
elif h < 20:
    print("Less than 20")


if h > 50 and h < 20:
     print(h)
