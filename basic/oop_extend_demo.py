## 类的继承  my_dict 继承了 UserDict 。继承了属性和方
from collections import  UserDict

class Father(object):
    def run(self):
      print("run in father")

class Son(Father):
    def run(self):
      # """继承了Father 的run 方法 进行调用"""
        super().run()
        print("run in son")
#
obj=Father()
obj.run()
obj2=Son()
obj2.run()

## 混入  减少多重继承的利用使用 混入 （Mix-in）
## 混入 Mix-in 是指 多继承的语法，为现有类增加新的方法
## 混入不定义新的属性，只包含方法
## 混入便于重用 ，但绝不能实例化
## 混入类一般的类名称后增加Mixin



# """类的装饰器"""
# classmethod 装饰器
    # classmethod 可以是实例的方法定义为类的方法 ，用于类直接调用
    # * cls 表示当前操作的类本身，可以使用Klass.func() 调用。
    # self 固定参数，为实例化对象

class Klass:

    ## 用途： 不需要进行实例化 直接调用类方法
        @classmethod
        def func(cls):
            print("classmethod")

  # staticmethod 装饰器  静态方法   staticmethod 修饰的方法不需要使用self或者cls
        @staticmethod
        def finc_2():
            print("staticmethod")



Klass.func()
Klass.finc_2()

class Class_3:
    # property 装饰器 (属性)   可以很快速的作为属性读取  。但是无法进行属性直接赋值。 必须实例化后调用
    ### 需要 用 property 装饰的方法调用setter 方法进行装饰 进行属性赋值
        @property
        def func_3(self):
           return  self.name
        @func_3.setter
        def func_4(self,value):
            self.name=value

Klass.func()
Klass.finc_2()

##  实例化
pro=Class_3()
##  赋值
pro.func_4="property"
##调用方法
print(pro.func_3)





