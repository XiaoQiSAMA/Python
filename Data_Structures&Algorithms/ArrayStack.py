"""使用适配器模式 通过list类实现栈"""

'''定义一个异常类，用来触发list类的IndexError异常'''
class Empty(Exception):
    pass

'''栈类'''
class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):          #入栈
        self._data.append(e)

    def top(self):              #返回栈顶的值
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):              #出栈
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

'''自定义栈实现数据的逆置'''

def reverse_file(filename):

    S = ArrayStack()
    with open(filename, 'w') as f:                 #入栈
        for line in f:
            S.push(line.rstrip('\n'))

    with open(filename, 'w') as f:                 #出栈
        while not S.is_empty():
            f.write(S.pop() + '\n')

'''自定义栈实现分隔符匹配算法'''
def is_matched(expr):

    lefty = '([{'
    righty = ')]}'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()















