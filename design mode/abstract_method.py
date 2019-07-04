'''
类似接口，在基类中实现的方法
'''
import abc
class fruits(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def eat(self):
        """基类方法，不用实现"""

class apple(fruits):
    def eat(self):
        print('eat!')

apple_1 = apple()
apple_1.eat()