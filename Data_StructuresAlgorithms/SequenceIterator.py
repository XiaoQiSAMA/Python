"""适合任何序列的迭代器"""

class SequenceIterator:

    def __init__(self, squence):
        self._squ = squence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._squ):
            return self._squ[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        return self