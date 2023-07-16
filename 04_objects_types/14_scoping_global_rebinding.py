count = 0

def show_count():
    print(count)


def set_count(c):
    count = c



show_count()
set_count(5)
show_count()


def set_count(c):
    global count
    count = c

show_count()
set_count(5)
show_count()


