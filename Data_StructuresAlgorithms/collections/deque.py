from collections import deque
import itertools
def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1)) #islice(iterable,stop)
    d.appendleft(0)
    s = sum(d)
    print(list(it))
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n

for i in moving_average([40, 30, 50, 46, 39, 44]):
    print(i)