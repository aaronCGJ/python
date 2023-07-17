## py可以为数学进行画图和函数计算
# ##  解决数学问题导入
from sympy import Symbol, Derivative
from sympy.plotting import plot

##  求导数
x=Symbol('x')
y=x*x+3*x+10
d=Derivative(y,x)
d.doit()
print(d.doit())
d.doit().subs({x:10})
print(d.doit().subs({x:10}))




