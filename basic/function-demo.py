import time


#商品
products=[[1000,"iphone","单价",12000],[1002,"ipad","单价",15000]]
## 购物车 "product_id,product price
carts={1000:100,1002:20}

def idtoname(product_id):
        for pro in products:
             if  pro[0]==product_id:
                return pro
                break

def idtoprice(product_id):
        for pro in products:
               if pro[0]==product_id:
                   return  pro
                   break
totalMoney=0
def queryproduct(totalMoney:int):
         for key,count in carts.items():
                product=   idtoname(key)
                cart=idtoprice(key)
                pro_total=product[3] * count
                print(f"产品：{product[1]}，单价：{product[3]},购买数量：{count},总价{product[3]*count}")
                totalMoney += pro_total
         return totalMoney

Money=queryproduct(totalMoney)
print(Money)

# 高阶函数  map()  filter() …… EX：

def add(number):
    return (number*number)


for i in map(add,range(5)):
    print(i)

# partial() 偏函数 可以用来固定函数参数。用新的函数来代替。


## 装饰器语法 @  EX: 执行原函数。 装饰器的作用，类似鱼java的注解。可以作为原函数意外的调用



def time_it(func):
    def warpper():
        start=time.time()
        func()
        end=time.time()
        print(f" func() time_fun 执行了{start-end}秒")
    return warpper


@time_it
def work():
    print("func 开始执行")
    time.sleep(1)
    print("func 结束执行")

work()


