## if 判断  需要顶格
var1='sss';
var2='s'

if(var1.__eq__('ss')):
    print("匹配")
elif var2.endswith('s'):
    print("ZOU了elif")
else:
    print("不匹配")

## match 语法
http_status=400
match http_status:
    case 400:
        print(f"{http_status}!")


