import argparse
# 执行方式
parser=argparse.ArgumentParser(description="number")
parser.add_argument("number","100")
args=parser.parse_args()
print(f"number={args.number}")