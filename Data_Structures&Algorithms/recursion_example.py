"""线性递归"""

'''元素序列递归求和'''

def line_sum(S, n):
    # 时间复杂度O(n)
    if n == 0:
        return n
    else:
        return line_sum(S, n - 1) + S[n - 1]


'''递归逆置序列'''

def reverse(S, start, stop):
    #时间复杂度O(n)
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)



'''递归计算n次幂'''

def power_1(x, n):
    # 时间复杂度O(n)
    if n == 0:
        return 1
    else:
        return x * power_1(x, n - 1)

'''使用重复的平方计算幂函数'''

def power_2(x, n):
    if n == 0:
        return 1
    else:
        p = power_2(x, n // 2)

        reault = p * p
        if n % 2 == 1:
            reault *= x
        return reault