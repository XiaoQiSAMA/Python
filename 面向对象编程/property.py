"""
主动计算(Eager Calculation):更新特性值时，其他特性值立即被重新计算
延迟计算(Lazy Calculation):仅当访问特性时，才触发计算过程
"""


#定义字符串的表示方法
class Hand:
    def __str__(self):
        return ','.join(map(str, self.card))
    def __repr__(self):
        return f"{self.__class__.__name__}({**self.__dict__}, {','.join(map(repr, self.card))})"
    

#延迟计算特性
class Lazy_Hand(Hand):
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self._cards = list(cards)
    
    @property
    def total(self):
        delta_soft = max(c.soft - c.hard for c in self._cards)
        hard_total = sum(c.hard for c in self._cards)
        if hard_total+dealer_card <= 21: return hard_total+dealer_card
        return hard_total
    @property
    def card(self):
        return self._cards
    @card.setter
    def card(self, aCard):
        self._cards.append(aCard)
    @card.deleter
    def card(self):
        self._cards.pop(-1)


#主动计算特性  total的属性是由主动计算实现的
class Eager_Hand(Hand):
    
    def __init__(self, dealer_card,*cards):
        self.dealer_card = dealer_card
        self.total = 0
        self._delta_soft = 0
        self._hard_total = 0
        self._cards = list()
        for c in cards:
            self.card = c
    
    @property
    def card(self):
        return self._cards

#setter deleter 特性    
    @card.setter
    def card(self, aCard):
        pass

    @card.deleter
    def card(self):
        pass



"""属性"""
'''
__setattr__() 属性的创建和赋值
__getattr__() 1.已赋值:不被调用，直接返回属性值
              2.未赋值:使用该函数的返回值
              3.找不到属性返回AttributeError
__delattr__() 删除属性
__dir__() 返回属性名称列表


*扩展类:重写__setattr__(),__delattr__()使其几乎不可变，也可使用__slots__替换内部__dict__对象
*封装类:提供对象属性访问的代理实现。
'''

