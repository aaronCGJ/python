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



