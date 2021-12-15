# 变量
# 命名规则：大小写字母，数字，_,不能以数字开头，不能是关键字

# 查看python中的关键字
import keyword

print(keyword.kwlist)

# 定义就要赋值
# 定义的时候，不需要指定类型，可以自动判断
a = 1
print(type(a))

# python是动态数据类型
a = 1.1
print(type(a))

# print 函数
# 将输出内容打印到控制台
# 并且可以打印多个值
print(a, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# 不换行打印
# print 中end默认\n
print("hello", end="")
print("yes")

# 注释
# 单行注释
'''
'''
"""
多行注释
用于文档说明
"""

# python中基本数据类型
"""
5大：
整型 int
浮点 float
字符串 str
布尔 bool
空类型 NoneType
"""

# 字符串，不严格区分单双引号
str = 'hello'
str1 = "world"
print(str, type(str))
print(str1)

# bool 首字母大写
bool1 = True
bool2 = False
print(bool1, type(bool1))
print(bool2)

# 空类型
none = None
print(none, type(none))

# 类型的转换
# 调用对应的 类型方法
str4 = '12'
print(str4, type(str4))
i1 = int(str4)
print(i1, type(i1))

str4float = float(str4)
print(str4float, type(str4float))

str4bool = bool(str4)
print(str4bool, type(str4bool))

# 字符串常用的方法
str1 = 'java scala sparrk'
print(str1.split(" "))  # 返回一个list

# 切片
# [起始位置:结束位置:步长]
# [起始，结束]
# 起始位置默认是第一个字符，结束位置默认是最后一个字符 步长默认为1
print(str1[5:11])  # 相当于java中substring

# 字符串倒转
print(str1[::-1])

# 步长表示 隔几个元素取一次
# 步长也可以是负的
print(str1[1:9:2])
print(str1[4:10:3])

# 索引
# 注意索引越界的问题
print(str1[6])
print(str1[-3])  # 表示从右往左数

# 查看字符串的长度
print(len(str1))

'''

'''
str2 = '  \t \n \r       gg  hh         ii  kcoie             k'
print(str2.strip())  # 去除字符串左右的空格，左右两边的隐藏字符

# 格式化字符串

# 定义一个模板
# {} * {} = {}
a = 1
b = 2
str_format = '{} * {} = {}'
print(str_format.format(a, b, a * b))

# %d * %d = %d
# %d 表示数字
# %s 表示字符串
# %f 表示小数
print('%d * %d = %d'%(a,b,a*b))

# 控制输出三位小数
f = 1.2222254878555
print('%.3f' % f)

#算术运算
i=10
j=3
print(i ** j)#i的j次方
print(i // j)#向下取整
print(2 ** 3  ** 2)#2的9次方，3的2次方，2的9次方
print()

#逻辑运算  与或非
"""
&   | 
and or
"""

#
