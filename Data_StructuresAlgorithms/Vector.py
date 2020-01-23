"""定义一个简单的多维向量类"""
class Vector:

    def __init__(self, d):
        '''创建初始d维向量'''
        self._coords = [0] * d

    def __len__(self):
        '''返回向量的维数'''
        return len(self._coords)
    
    def __getitem__(self,j):
        '''返回第j个向量的坐标'''
        return self._coords[j]

    def __setitem__(self, j, val):
        '''给第j个向量值'''
        self._coords[j] = val

    def __add__(self, other):
        '''返回两个向量相加的值'''
        if len(self) != len(other):             #依靠 __len__方法
            raise ValueError('dimension must agree')
        reault = Vector(len(self))              #实例全为0的多维向量
        for j in range(len(self)):
            reault[j] = self[j] + other[j]
        return reault

    def __eq__(self, other):
        '''如果向量和另一个向量有相同的坐标返回True'''
        return self._coords == other._coords

    def __ne__(self, other):
        '''如果向量和另一个向量坐标不同则返回True'''
        return not self == other                #依赖于 __eq__定义

    def __str__(self):
        '''对向量字符串化'''
        return '<' + str(self._coords)[1:-1]+'>'

if __name__ == '__main__':
    v = Vector(5)
    v[0] = 2
    v[3] = 4
    print(v)
    u = v + v
    print(u)
    total = 0
    for i in u:
        total += i
    print(total)