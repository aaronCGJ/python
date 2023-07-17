## BaseException 所有内置异常的基类 不直接使用
### 自定义的异常 继承 Exception
## 异常补获   格式：
         # try :
         #     可能产生异常的代码
         #     except 「异常」：
         #     捕获制定的异常后运行的代码

mum1="1"
mum2="zero"
try:
 num=mum1/mum2
except Exception as message:
     print(message)
else:
    print('else')
finally:
    print("finally")


## 业务自定义的异常 nameError
name = "aaron"
class nameError(Exception):
    def __init__(self,message):
        self.message=message
    @property
    def msg(self):
        return f"名字权限受控{self.message}"

try:
    if(name=="aaron"):
        raise  nameError(name)
except nameError as e:
    print(e.msg)


