### 文件打开学习 open()
import pprint

# filer_data=open("/Users/aaron.chen/data/update_vendor/更新设备机柜位置_1684911506674.txt",mode="r",encoding="GBK")
# data_line=filer_data.readlines()
# filer_data.close()
# pprint.pprint(data_line )

write=open("/Users/aaron.chen/data/update_vendor/open_demo.text",mode='w',encoding="UTF-8")
write.write("人生苦短， 我来搞python!")
write.close()

read=open("/Users/aaron.chen/data/update_vendor/open_demo.text",mode='r',encoding="UTF-8")
pprint.pprint(read.readlines())
