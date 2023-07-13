## 函数demo
## 格式 : def 函数名([函数参数]):
##       函数体
##      retun 返回值
##      """ 三个双引号标示函数用途，作为说明。
##查看文档方法 函数内省功能 dir(foo)   EX : foo.__doc__


## 调用吧函数 函数名()


def foo():
    """我是函数说明"""
    print("function")
    print("foo")
print("不在函数体内")

foo().__doc__


## 匿名函数 借用lambda 表达式
data=lambda x:x+1
print(data(10))


## 函数和外部数据通信。通过参数传递..
## python 和java不一样的地方是，传递参数可以不按照顺序，但是需要制定形参的变量名

def f(str):  ## str形参
    print(f"传入，{str}")


f("number1") ## number1 实参
f("f3")

def deff(str:int,str2:int) ->float:
    return  str*str2

print(deff(10101,221))

## 不定长参数
## 电话本函数
## * 接收位置参数
## ** 接收关键字参数
def address_book(name,*telphone,alias_name=None,**custom):

    print(f"name:{name},tel:{telphone},alias_name:{alias_name},custom:{custom}")
    return name
data=  address_book("aaron",188,344,5667,"胖哥",家庭="幸福",性别="男")
print(data)










