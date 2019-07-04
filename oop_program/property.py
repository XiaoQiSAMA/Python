"""
主动计算(Eager Calculation):更新特性值时，其他特性值立即被重新计算
延迟计算(Lazy Calculation):仅当访问特性时，才触发计算过程
"""


# #定义字符串的表示方法
# class Hand:
#     def __str__(self):
#         return ','.join(map(str, self.card))
#     def __repr__(self):
#         return f"{self.__class__.__name__}({**self.__dict__}, {','.join(map(repr, self.card))})"
    

# #延迟计算特性
# class Lazy_Hand(Hand):
#     def __init__(self, dealer_card, *cards):
#         self.dealer_card = dealer_card
#         self._cards = list(cards)
    
#     @property
#     def total(self):
#         delta_soft = max(c.soft - c.hard for c in self._cards)
#         hard_total = sum(c.hard for c in self._cards)
#         if hard_total+dealer_card <= 21: return hard_total+dealer_card
#         return hard_total
#     @property
#     def card(self):
#         return self._cards
#     @card.setter
#     def card(self, aCard):
#         self._cards.append(aCard)
#     @card.deleter
#     def card(self):
#         self._cards.pop(-1)


# #主动计算特性  total的属性是由主动计算实现的
# class Eager_Hand(Hand):
    
#     def __init__(self, dealer_card,*cards):
#         self.dealer_card = dealer_card
#         self.total = 0
#         self._delta_soft = 0
#         self._hard_total = 0
#         self._cards = list()
#         for c in cards:
#             self.card = c
    
#     @property
#     def card(self):
#         return self._cards

# #setter deleter 特性    
#     @card.setter
#     def card(self, aCard):
#         pass

#     @card.deleter
#     def card(self):
#         pass



"""属性"""

'''
__setattr__() 属性的创建和赋值
__getattr__() 1.已赋值:不被调用，直接返回属性值
              2.未赋值:使用该函数的返回值
              3.找不到属性返回AttributeError
__delattr__() 删除属性
__dir__() 返回属性名称列表
__new__() 允许创建未初始化的对象 可以在__init__()之前设置对象属性
__dict__ 类中表达属性的一个字典对象
__del__() 确保文件被关闭   eg: __del__ = close 保证__del__()同时也是close()方法

*扩展类:重写__setattr__(),__delattr__()使其几乎不可变，也可使用__slots__替换内部__dict__对象
*封装类:提供对象属性访问的代理实现。


'''

'''修饰符'''
'''
Descriptor.__get__(self, instance, owner) :instance参数来自被访问对象的self变量，
owner是拥有者类的对象。被类调用则未None。               返回修饰符的值
Descriptor.__set__(self, instance, value) :value为即将新赋的值
Descriptor.__delete__(self, instance): 实现属性值的删除
'''
#非数据修饰符
class UnitValue_1:
    def __init__(self, unit):
        self.value = None
        self.unit = unit
        self.dafault_format = '5.2f'

    def __set__(self, instance, value):
        self.value = value
    def __str__(self):
        return "{value:{spec}} {unit}".format(spec=self.dafault_format, **self.__dict__)
    def __format__(self, spec = '5.2f'):
        if spec == '': spec = self.dafault_format
        return "{value:{spec}} {unit}".format(spec=spec, **self.__dict__)
'''定义了简单的数值对，一个是可变的(数值)，一个是不可变的(单位)'''
#example
class RTD_1:
    rate = UnitValue_1("kt")
    time = UnitValue_1("hr")
    distance = UnitValue_1("nm")
    def __init__(self,rate=None,time=None,distance=None):
        if rate is None:
            self.time = time
            self.distance = distance
            self.rate = distance / time
        if time is None:
            self.rate = rate
            self.distance = distance
            self.time = distance / rate
        if distance is None:
            self.rate = rate
            self.time = time
            self.distance = rate * time
    def __str__(self):
        return f"rate : {self.rate} time : {self.time} distance : {self.distance}"

m1 = RTD_1(rate=5.8,distance=12)
print(m1)  
#rate :  5.80 kt time :  2.07 hr distance : 12.00 nm
print('Time:',m1.time.value, m1.time.unit)  
#Time: 2.0689655172413794 hr

#数据修饰符
class Unit:
    conversion = 1.0
    def __get__(self, instance, owner):
        return instance.kph * self.conversion       #kph : 千米每小时
    def __set__(self, instance, value):
        instance.kph = value / self.conversion
        
#实现标准单位和非标准单位的互转


class Knots(Unit):
    conversion = 0.5399568

class MPH(Unit):
    conversion = 0.62137119

#非标准单位


class KPH(Unit):                                #定义标准
    def __get__(self, instance, owner):
        return instance._kph
    def __set__(self, instance, value):
        instance._kph = value

class Measurement:
    kph = KPH()
    knots = Knots()
    mph = MPH()
    def __init__(self, kph=None, knots=None, mph=None):
        if kph: self.kph = kph
        elif mph: self.mph = mph
        elif knots: self.knots = knots
        else:
            raise TypeError
    def __str__(self):
        return f"rate: {self.kph}, kph: {self.mph}, mph: {self.mph}, knots: {self.knots}"

m2 = Measurement(knots=5.9)
print(m2)
#rate: 10.92680006993152, kph: 6.789598762345432, mph: 6.789598762345432, knots: 5.9
print("KPH:" + str(m2.kph),"MPH:" + str(m2.mph))
#KPH:10.92680006993152 MPH:6.789598762345432

