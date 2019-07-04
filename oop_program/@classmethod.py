"""类的属性及方法的调用"""

class A:
    def __Init__(self, a):
        self.a = a
    # @classmethod
    def q(self):
        print("q")
        self.e()
    # @classmethod
    def e(self):
        print("w")

class B:
    def e(self):
        # A.q()
        # A.a = 1
        # print(A.a)
        print('e')

# b = B()
# b.e()

"""多继承"""
'''多继承下，按照排序寻找函数位置'''
class C(B,A):
    pass
c = C()
c.q()
