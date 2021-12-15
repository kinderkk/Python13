# 函数：实现类某一些特定功能的代码
'''不需要权限修饰符
    不需要返回值类型
def 函数名(参数1，参数2……):
    代码块
    代码块
    #如果需要返回值，直接return
    return 返回值
'''


# 计算1~n的和
def sum2N(n1):
    sum = 0
    i = 1
    while i <= n1:
        sum += i
        i += 1
    return sum


res = sum2N(100)
print(res)


# 计算n的阶层
def Jc(n):
    res = 1
    while n >= 1:
        res *= n
        n -= 1
    return res


print(Jc(5))


# 递归
def jc2(n):
    if n == 1:
        return 1
    return n * jc2(n - 1)


j = jc2(5)
print(j)


# 函数参数的类型
# 位置参数（必选参数）、默认参数、可变参数、关键字参数、命名关键字参数

# 默认参数
# 计算x 的y次方 ，如果不传入y，则默认是2
def cf(x, y=2):
    return x ** y


d = cf(2)
print(d)
print(cf(2, 9))


# 可变参数
# 传入n1就返回n1
# 传入n1 n2，就返回n1 + n2
# args 是参数名，如果要操作传入的参数，可以对args（相当于参数构成的tuple）进行遍历
def sunN(*args):
    print(args, type(args))
    sum = 0
    for i in args:
        sum+=i
    print(sum)

sunN(1,2,3)

#关键字参数
#注册函数：
#name，age，addr（可选），phone（可选）
def register(name,age,**kwlist):
    print(kwlist,type(kwlist))

register("hh",'20',addr='rr',phone='18888888')

#命名关键字参数
#name，age，gender（必选），addr（可选），phone（可选）
def register1(name,age,**kwlist):
    if 'gender' in kwlist.keys():
        print(kwlist,type(kwlist))
    else:
        print("必须有性别")
register1("hh",'20',addr='rr',phone='18888888')

def register3(name,age,*,gender,**kwlist):
    print(gender,kwlist)

register3("hh",'20',gender='male')