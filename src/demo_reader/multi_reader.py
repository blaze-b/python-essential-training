class MultiReader:
    def __init__(self, file_name):
        self._file_name = file_name
        self._file = open(file_name, 'rt')

    def close(self):
        self._file.close()

    def read(self):
        return self._file.read()
