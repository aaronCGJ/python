## 类的写法 class 修饰符， 首字母大写 继承 来源在 括号 Coofee(objec)  object 可省略 累的实例化  ab=Coffee()  ab为Coffee 的实例化对象

class Coffee:
    water=1
    milk=1

    ## 类中定义方法  需要第一个参数为self . self 固定参数，为对象本身
    def add_water(self):
        self.water=5

mocha=Coffee
mocha.add_water(Coffee)
print(mocha.water)




