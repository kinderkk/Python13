# 文件IO
# open函数
# f1 = open("students.txt",mode='r',encoding='utf8')
# '''
# read(n)  读n行
# readline 读一行
# readlines 读全部
# '''
# print(f1.read(10))
# print(f1.readline())
# print(f1.readline())
# print(f1.readlines())
#
# #关闭文件
# f1.close()

# 写
'''

'''
# f2 = open("newfile.txt",mode='w',encoding='utf8')
# f2.write('abc\n')#必须传入字符串
# f2.write('abc\n')#必须传入字符串
# f2.write('abc\n')#必须传入字符串
# f2.writelines(['hhh\n','hhh','hhh','hhh','hhh','hhh','hhh'])
# f2.close()
#
# with open('students.txt',mode='r',encoding='utf8') as f3:
#     with open('newfile.txt',mode='a',encoding='utf8') as f4:
#         f4.writelines(f3.readlines())

# 操作mysql
# 先导入
import pymysql

conn = pymysql.connect(user='root', password='123456', host='master', port=3306, db='student')

# 创建游标，类似于statement
cursor = conn.cursor()
# 返回最后查询出来的条数
t = cursor.execute("select id,name,age from student where clazz like %s and gender = %s", ('理科%', '男'))
print("总计记录数：", t)

# print(cursor.fetchone())  # 返回一条记录
# print(cursor.fetchmany(3))  # 返回n条记录
# print(cursor.fetchall())  # 返回所有

for i in range(t):
    print(cursor.fetchone())

# cursor.close()
# conn.close()

with pymysql.connect(user='root', password='123456', host='master', port=3306, db='student') as conn:
    with conn.cursor():
        t1 = cursor.execute("select id,name,age from student where clazz like %s and gender = %s", ('理科%', '男'))
        for i in range(t1):
            print(cursor.fetchone())
        conn.rollback()  # 发生异常进行回滚
        conn.commit()  # 没有异常进行提交


#格式化日期字符串
from datetime import datetime

