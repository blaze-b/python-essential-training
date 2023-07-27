import sys

import root.multi_reader as reader
import root.module as module
# Add that path to the python path and all the modules will be activated
# Provide the absolute path
sys.path.append("D:\code\python-essential-training\src\python_root")


def test():
    module


def multi_reader_test():
    r = reader.MultiReader("root/__init__.py")
    print(r.read())
    r.close()


if __name__ == '__main__':
    sys.exit(test())
    multi_reader_test()
