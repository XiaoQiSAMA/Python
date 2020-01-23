"""为游戏存储高分"""

class GameEntry:

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return f"({self._name}, {self._score})"


"""高分排行榜"""

class Scoreboard:

    def __init__(self, capacity=10):

        self._board = [None] * capacity         #创建空列表，默认长度为10
        self._n = 0                             #计数表中元素个数

    def __getitem__(self, item):

        return self._board[item]

    def __str__(self):

        return '\n'.join(str(self._board[k]) for k in range(self._n))

    def add(self, entry):
        score = entry.get_score()

        good = self._n < len(self._board) or self._board[-1].get_score < score

        if good:
            if self._n < len(self._board):
                self._n += 1

            j = self._n - 1
            if j > 0 and self._board[j] < score:
                self._board[j] = self._board[j - 1]
                j -= 1
            self._board[j] = entry
