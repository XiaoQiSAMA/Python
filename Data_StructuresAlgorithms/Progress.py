"""通用数字数列类"""


class Progression:
    '''普通数字数列： 0，1，2，3，4...'''

    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progress(self, n):
        # 打印n个数列
        print(' '.join(str(next(self)) for j in range(n)))


"""产生等差数列的类"""

class ArithmeticProgression(Progression):

    def __init__(self, increment=1, strat=0):
        '''
        :param increment: 等差值(默认为 1 )
        :param strat:   开始的数值
        '''
        super().__init__(strat)
        self._increment = increment

    def _advance(self):
        self._current += self._increment


'''产生等比数列的类'''
class GeometricProgression(Progression):

    def __init__(self, base = 2, start = 1):
        '''
        :param base: 比值
        :param start:  开始的数值
        '''

        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base


"""一个斐波那契数列"""
class FibonacciProgression(Progression):

    def __init__(self, first = 0, second = 1):
        '''
        :param first: 第一个数值
        :param second: 第二个数值
        '''

        super().__init__(first)
        self._prev = second - first             #在first之前构造一个变量

    def _advance(self):
        '''当前的值赋予前一个，把当前的值和之前的值相加赋予当前'''
        self._prev, self._current = self._current, self._prev + self._current


#test
if __name__ == '__main__':
    print('Default progression')
    Progression().print_progress(10)

    print("等差数列(差值为5)")
    ArithmeticProgression(5).print_progress(10)

    print('等差数列(差值为5，从2开始)')
    ArithmeticProgression(5, 2).print_progress(10)

    print('等比数列(默认数值)')
    GeometricProgression().print_progress(10)

    print('等比数列(比值为3)')
    GeometricProgression(3).print_progress(10)

    print('斐波那契数列(默认数值)')
    FibonacciProgression().print_progress(10)

    print('斐波那契数列(从4 ，6开始)')
    FibonacciProgression(4, 6).print_progress(10)