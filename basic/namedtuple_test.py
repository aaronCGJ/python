from collections import namedtuple,Counter

Point=namedtuple('Point',['x','y'])
p1=Point(11,y=22)
p1.x is p1[0]




class Point_2D(Point):
    """魔术方法，自定义"""
    def __add__(self, other):
        self.other_x,self.other_y=other
        return  self.x+self.other_x,self.y+self.other_y
    def __sub__(self, other):
        self.other_x,self.other_y=other
        return  self.x-self.other_x,self.y-self.other_y

    def __mul__(self, other):
        self.other_x, self.other_y = other
        return self.x *self.other_x, self.y *self.other_y

p1=Point_2D(10,y=5)
p2=Point_2D(x=10,y=5)
print(p1*p2)

### 双端队列 deque
## Counter 对象， 计数器工具

cnt=Counter()
for word in ['be',2,1,4,5,4,6,7,8,13,'2']:
    cnt[word]+=1
print(cnt)
print(dir(Counter))



