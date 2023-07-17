## 定义属性和方法
## self 实例属性


##coffee 类
class CoffeeMixin:
    def __init__(self):
        self.mumber=0
    def addCoffee(self,nums):
        self.mumber = nums
        if(nums<0):
            return f"输入coffee的量:{self.mumber}有错误:"

        return f"add coffee:{self.mumber} ML "

## 水类
class WaterMixin:
    def __init__(self):
        self.temperature=None
        self.volume=0

    def addwater(self,nums,temp):
        self.volume=nums
        if int(self.volume)<0:
            return f"add water : {self.volume} 异常"

        if temp=="cold":
            self.temperature="cold"
        elif temp=="hot":
            self.temperature="hot"
        return  f"add{self.temperature} water {self.volume} ML"

## 牛奶类
class MilkMixin:
        def  __init__(self):
            self.volume=0
            self.temperature=None

        def addmilk(self,nums,temp):
            self.volume=nums
            self.temperatur=temp
            if int(self.volume)<0:
                return  f"输入 coffee:{self.volume} 异常"

            return f"add {self.volume} {self.temperatur} Milk  "



class Coffee(WaterMixin,CoffeeMixin,MilkMixin):
    """初始化属性方法"""
    def __init__(self,water=-1,water_temp="cold",milk=-1,milk_temp="cold",coffee=-1):
        self.water=water
        self.water_temp=water_temp
        self.milk=milk
        self.milk_temp=milk_temp
        self.coffee=coffee
        self.prescription=[]

        # if int(self.water > 0) and self.water_temp != None:
        self.prescription.append(super().addwater(self.water, self.water_temp))
        # if (int(self.milk > 0) and self.milk_temp != None):
        self.prescription.append(super().addmilk(self.milk, self.milk_temp))
        # if (int(self.coffee > 0)):
        self.prescription.append(super().addCoffee(self.coffee))

    def showPrescription(self):
        for i in self.prescription:
            print(i)


coff_demo=Coffee(water=100,water_temp="hot",milk=50,milk_temp="cold",coffee=50)
coff_demo.showPrescription()





