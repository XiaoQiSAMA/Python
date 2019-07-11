
def binary_search(data, target, low, high):
    '''
    这个二分查找仅考虑data[low]~data[high]这部分
    '''
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

a = [1, 3, 5, 6, 7, 9, 11, 23, 24]
t = 23
print(binary_search(a, t, 1, 9))