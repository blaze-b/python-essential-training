import sys

f = None


def read_file_details(path):
    f = open(path, mode='rt', encoding=sys.getdefaultencoding())
    for line in f:
        sys.stdout.write(line)
    return f


try:
    f = read_file_details(sys.argv[1])
except (IndexError, NameError, FileNotFoundError) as e:
    print(e, file=sys.stderr)
    path = "09_io_file/wasteland.txt"
    f = read_file_details(path)
finally:
    if f is not None:
        f.close()
