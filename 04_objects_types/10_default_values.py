import time

current_time = time.ctime()

print("Time = ", current_time)


def show_default(arg=time.ctime()):
    print(arg)


count = 0

while count < 10:
    show_default()
    count += 1
