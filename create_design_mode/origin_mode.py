"""原型模式"""
'''
将现有的对象复制出新的对象并对其修改
'''
import sys
import copy

class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x ,y):
        self.x = x
        self.y = y 

def make_object(Class, *args, **kwargs):
    return Class(*args, **kwargs)

#七种复制实例
point1 = Point(1, 2)
point2 = eval("{}({}, {})".format("Point", 1, 2))  #有危险的
point3 = getattr(sys.modules[__name__], "Point")(3, 6)
point4 = globals()["Point"](4, 8)
point5 = make_object(5, 10)
point6 = copy.deepdopy(point5)
point6.x = 1
point6.y = 2
point7 = point1.__class__(7, 14)   #可以复制任何一个point

