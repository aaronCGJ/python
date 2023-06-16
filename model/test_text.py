import pprint
from tinydb import  TinyDB
from tinydb import  Query

# with open("/Users/aaron.chen/data/update_vendor/更新设备机柜位置_1684911506674.txt") as text:
#     file_data=text.readlines()
#     # print(file_data)
#     # print(file_data.count("\n"))
#     pprint.pprint(file_data)

###TinyDB使用 通讯录案例
# db=TinyDB("/Users/aaron.chen/data/pyDb.json")
# friend_1={'name':'aaron','source':'同事','电话':'1999'}
# friend_2={'name':'aaron1','source':'朋友','电话':'1998'}

# db.insert_multiple([friend_1,friend_2])
# print(db.all())
# friend=Query()
# friend_info=db.search(friend.name=='aaron')
# varw='a'
# print(type(varw))
# help(str)
# print(friend_info[0]['name'])
# var2=varw.__add__("s");
# print(var2.capitalize()) # 大写
# print(friend_info[0]['source'])
# print(friend_info[0][varw])




