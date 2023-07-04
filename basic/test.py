import argparse
# 执行方式
# parser=argparse.ArgumentParser(description="number")
# parser.add_argument("-number1",type=int,default=1,help="输如一个数字")
# args=parser.parse_args()
# print(f"number={args.number1}")
#


# print("{B} than {U}".format(U="two", B="one"))

B='one'
u='two'
number=123.4567
## 精度和长度转换  f-String 写法
number2=float(f"{number:.3f}")
print(f"{number2:010}")

