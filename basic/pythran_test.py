##  混合编程

## Pythran 进行代码转换  .py 转换 .hpp  (C#)
# 格式: pythran -e  python代码.py -p pythran.optimizations.ConstantFolding  - o 输出格式代码.hpp

## cpp 引入 hpp 代码块
#####cpp start #######
## # include "cli_foo.hpp"
## using namespace __pythran_cli_foo;
## int main()
##  {    foo()()
#           return 0;
#    }
#####cpp end #######

### cpp 和hpp 转为可执行文件 cli_foo
##格式：    `pythran-config --compiler --cflags` -std=c++11 cli_foo.cpp -o cli_foo