from itertools import count, islice


def sequence():
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


def read_series(filename) -> list:
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]


def write_sequence(filename, num) -> None:
    """Write Recaman's sequence to a text file."""
    with open(filename, mode='wt', encoding='utf-8') as f:
        f.writelines(f"{r}\n"
                     for r in islice(sequence(), num + 1))


print(write_sequence("09_io_file/recman_1.dat", 100))

print(read_series("09_io_file/recman_1.dat"))
