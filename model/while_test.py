## while 语法

var=[1,2,3,4]

# i,j,count=0,1,1
# while i<j:
#     i+=1
#     j+=1
#     print(i+j)
#     count += 0.1
#     if count>10000:
#          print("我执行报废了")
#          break

# 序列

list=[i for i in range(1,100)]
list2=[]
list3=[]
for i in list :
     if i%7==0:
         list2.append(i)

     else:
          list3.append(i)
print(list2)
print(list3)


