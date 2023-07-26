"""Demonstrate raiding a refrigerator."""


from contextlib import closing


class RefrigeratorRaider:
    """Raid a refrigerator"""

    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print(f"Finding {food}...")
        if food == 'deep fried pizza':
            raise RuntimeError("Health warning!")
        print(f"Taking {food}")

    def close(self):
        print("Close fridge door.")


def raid(food):
    r = RefrigeratorRaider()
    r.open()
    r.take(food)
    r.close()


def raid_with_closing(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)


def test_function_1():
    raid('bacon')
    raid('deep fried pizza')


def test_function_2():
    raid_with_closing('bacon')
    raid_with_closing('deep fried pizza')


test_function_2()
