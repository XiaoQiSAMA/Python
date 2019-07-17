"""适配器模式用list类实现队列"""

'''当队列为空，front或dequeue被调用，返回Empty异常实例'''
class Empty(Exception):

    pass


'''循环使用数组的队列'''
class ArrayQueue:

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):             #判断队列是否为空
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):                      #出队列

        if self.is_empty():
            raise Empty('Queue is empty')

        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):                   #入队列
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size -= 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data = old[walk]
            self._front = (walk + 1) % len(old)
        self._front = 0