'''计算第n个斐波那契数'''


#效率太低
def bad_fibonacci(n):

    if n <= 1:
        return n

    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)


#线性递归计算
def good_fibonacci(n):

    if n <= 1:
        return (n, 0)

    else:
        (a, b) = good_fibonacci(n - 1)
        return (a + b, a)
