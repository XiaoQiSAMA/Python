"""链表"""

'''单向链表实现栈
用链表的头部实现栈顶，因为只有在头部才能在一个常数时间内有效的插入和删除元素，因为所有的栈操作都会影响栈顶
'''


class LinkedStack:

    class _Node:
        # 创建的私有类
        __slots__ = '_element', '_next'  # 约束,提高内存利用率

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):

        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    # 入栈
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    # 栈顶元素
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    # 出栈
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


# 定义的异常类
class Empty(Exception):
    pass


'''单向链表实现队列'''


class LinkedQueue:

    class _Node:
        # 创建的私有类
        __slots__ = '_element', '_next'  # 约束,提高内存利用率

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):

        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head._element = self._head._next
        self._size -= 1
        if self.is_empty():                 #当队列为空时，让尾指针为空
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest                 #更新尾指针的位置
        self._size += 1

