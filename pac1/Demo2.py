# 数据容器 相当于java中集合
# 四大数据容器
# 列表：list、元祖tuple，字典dict，集合set


# 列表list
# 特点：
# 1.list中的每个元素的类型可以不唯一
# 2.list中的元素可以重复
# 3.list是可变的，里面的元素可以修改
# 4.list是有序的
# 定义：
list1 = [1, 2, 34, 5, 6, 7, 'a', 'b', True, False]
print(list1, type(list1))

# list常用操作
# 取元素
# 通过下标
print(list1[5])

# 切片
# [起始位置:结束位置:步长]
# [起始，结束]
# 起始位置默认是第一个字符，结束位置默认是最后一个字符 步长默认为1
print(list1[1:6])
print(list1[-4::])
# 反转
print(list1[::-1])

# 修改元素
list1[7] = 'A'
print(list1)

# 增加元素
list1.append('last')
list1.insert(1, 1.1)
print(list1)

# 删除元素
print(list1.pop())  # 默认将最后一个元素返回
list1.remove(1.1)  # 根据指定的值，移除元素  只会移除一次
print(list1)
del list1[5]
print(list1)

# 其他操作
# 排序
list2 = [2, 4, 1, 7, 5, 4, 9, 6, 5]
list2.sort()
list2.sort(reverse=True)  # 倒序
print(list2)

# 查找元素
list2.index(7)

#
print(11111111111111111111111)
list2 = [2, 4, 1, 7, 5, 4, 9, 6, 5]
list3 = [5, 7, 2]
print(list2 + list3)  # 不会改变原来的list2
list2.extend(list3)  # 会改变原来的list2
print(list2)

# 反转
list2.reverse()
print(list2)

# 统计1出现的次数
print(list2.count(1))

# 清空列表
list2.clear()
print(list2)

# tuple元祖（不可变）
'''
特点：
1.tuple中的每个元素的类型可以不唯一
2.tuple中的元素可以重复
3.tuple是不可变的
4.tuple是有序的
'''

# 定义：
tuple1 = (1, 2, 34, 5, 6, 7, 'a', 'b', True, False)
print(tuple1, type(tuple1))
# 元祖不支持修改

# 取元素
print(tuple1[1])

# 集合
# 定义
'''
特点：
1.set中的每个元素的类型可以不唯一
2.set中的元素不可以重复，会自动去重
3.set是可变的
4.set是无序的
'''
set1 = {1, 2, 34, 5, 6, 7, 'a', 'b', True, False}
print(set1, type(set1))

# print(set1[1])  无序，不能通过索引获取元素

set1.pop()
print(set1)
# 加的位置也是不固定的
set1.add(2)
set1.add(2)
set1.add(2)
set1.add(2)

# 集合的运算
# 交集  并集  差集…………
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
print(set2 & set1)
print(set2 | set1)
print(set2 - set1)

# 字典 dict  相当于 java中的map
# 特点：
# 1.字典里每一个元素都是k-v格式的
# 2.dict不支持使用index获取元素，都是通过key获取values
# 3.dict是可变的
# 4.dict的key不重复，是唯一的,key必须是不可变的(基本数据类型、元组)
# 5.如果key中同时存在 0 1 与 true false，会进行覆盖
# 6.查询速度不会随着元素的增多而变慢
# 定义
dict = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3',
    '0': '1',
    (1, 2, 3): 'tuple 1,2,3',
    # [4,5,6]:'list 4,5,6'
    True: "True",
    False: 'False',
    'kk2': 1,
    'kk3': 1.1,
    'kk4': [1, 2, 3],
    'kk5': {
        'kkk5': {
            'kkkk5': '12'
        }
    }
}
print(dict.get('kk5').get('kkk5').get('kkkk5'))

print(dict, type(dict))

# print(dict[1]) 不支持通过下标取元素
# 通过key取value
print('k1')

# 推荐使用get，获取元素
print(dict.get('k1'))
print(dict.get('kk1', '如果key不存在就返回'))

# 常见的操作
print(dict.keys())
print(dict.values())
print(dict.items())

# 遍历数据容器
list1 = [1, 2, 3, 4, 5, 6]
# for 变量名 in 数据容器
for i in list1:
    # 前面有四个空格
    print(i)

# 定义只有一个元素的元组时
tuple1 = (1,)
print(tuple1, type(tuple1))

tuple2 = (1, 2, 3, 4, 5)
for i in tuple2:
    print(i)  # 打印去重后的结果

dict1 = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3'
}
for i in dict1:
    print(i)  # 遍历出key
for kv in dict1.items():
    print(kv)
for k, v in dict1.items():
    print(k, v)

# 列表推导式
# 创建一个 1~10 的list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)

# 创建一个 1~100 的list
# range(起始位置:结束位置:步长)函数
print(range(1, 100, 1))
list100 = []
for i in range(1, 100, 1):
    list100.append(i)
    # print(i)
print(list100)

# 列表推导式
print([i for i in range(1, 100, 1) if i % 2 == 1])

#join方法与split方法相反
str1 = 'java,spark,python'
list3 = str1.split(",")
print(list3,type(list3))

str2 = "|".join(list3)
print(str2,type(str2))

#9*9乘法表
print("\n".join(["\t".join(["{} * {} = {}".format(i,j,i*j) for j in range(1,i+1)]) for i in range(1,10)]))