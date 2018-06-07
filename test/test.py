# 引用sys包获取系统路径
import sys

print("Python import mode")
print("命令行参数为：")
for i in sys.argv:
    print(i)
print("\n python 路径为", sys.path)

# 基本数据类型赋值
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

'''
Python中的字符串用单引号或双引号括起来,同时使用反斜杠转义特殊字符
字符串的截取的语法格式:
变量[头下标:尾下标]
Python的字符串不能被改变,向一个索引位置赋值,比如word[0]='m'会导致报错
'''
str = 'runoob'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始到结尾的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串

# Python使用反斜杠转义特殊字符,如果你不想让反斜杠发生转义,可以在字符串前面添加一个r,表示原始字符串:
print('Ru\noob')
print(r'Ru\noob')

'''
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。
'''

# 三个变量都指向同一个内存位置
a = b = c = 1
# 三个变量对应三个内存地址
a, b, c = 1, 2, "ruoob"

# 类型判断
print(type(a))
print(type(b))
print(type(c))
print(isinstance(a, int))


# isinstance 和 type的区别:type()不会认为子类是一种父类类型,isinstance()会认为子类是一种父类类型
class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))  # returns True
print(type(A()) == A)  # returns True
print(isinstance(B(), A))  # returns True
print(type(B()) == A)  # returns False

# del删除对象
del a
del b, c

# 数值运算,注:在混合计算时,Python会把整型转换成为浮点数
print(5 + 4)  # 加法
print(4.3 - 2)  # 减法
print(3 * 7)  # 乘法
print(2 / 4)  # 除法,得到一个浮点数
print(2 // 4)  # 除法,得到一个整数
print(17 % 3)  # 取余
print(2 ** 5)  # 乘方


