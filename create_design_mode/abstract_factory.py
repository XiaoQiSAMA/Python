"""抽象工厂模式"""
# 先建立一个类工厂，写好每个组件接口与参数
# 然后通过调用函数来给予工厂类参数
# 然后return对象
#! 工厂之间过于独立,容易产生名称冲突
'''Python 抽象工厂模式'''

class DiagramFactory:

    class Diagram:
        def __init__(self, width, height):
            pass
            
    class Text:
        def __init__(self, x, y, text, fontsize):
            pass


    @classmethod
    def make_diagram(Class, width, height):
        return Class.Diagram(width, height)
    
    @classmethod
    def make_Text(Class, x, y, text, fontsize):
        return Class.Text(x, y, text, fontsize)
