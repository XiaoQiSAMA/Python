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
        if 0 < self._size < len(self._data) // 4:       #如果元素个数小于数组长度的1/4，将数组缩减为1/2
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):                   #入队列
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        avail = (self._front + self._size) % len(self._data)                #计算入队列的值的索引位置
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):                 #重新创建一个数组，并将原数组的索引按入队顺序排序在新数组中+
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data = old[walk]
            self._front = (walk + 1) % len(old)
        self._front = 0


"""双端队列"""

'''Python Collection模块中的双端队列
from collections import deque
这种方法使用了循环数组组合到块中，而这些块本身又被组合到一个双向链表中

'''

'''使用环形数组实现双端队列'''
class ArrayDeque(ArrayQueue):
    def __init__(self):
        super(ArrayDeque, self).__init__()

    def last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def delete_first(self):
        super().dequeue()

    def delete_last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        index = (self._size - 1) % len(self._data)
        answer = self._data[index]
        self._data[index] = None
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:       #如果元素个数小于数组长度的1/4，将数组缩减为1/2
            self._resize(len(self._data) // 2)
        return answer

    def add_last(self, e):
        super().enqueue(e)

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1


