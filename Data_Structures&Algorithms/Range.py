"""实现自定义Range类"""


class Range:

    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step canot be 0')

        if stop == None:                        #格式为range(n)
            star , stop = 0, start              #格式为range(0, n)

        #计算有效的迭代长度
        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step


    def __len__(self):
        return self._length

    def __getitem__(self, k):                   #k为目录下标
        if k < 0:
            k += len(self)

        if not 0<= k <= self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step