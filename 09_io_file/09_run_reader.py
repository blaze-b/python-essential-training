"""Read and print an integer series."""
import sys


def read_series(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    series = []
    for line in f:
        a = int(line.strip())
        series.append(a)
    f.close()
    return series


def main(filename):
    series = read_series(filename)
    print(series)


if __name__ == '__main__':
    main("09_io_file/recman.dat")
