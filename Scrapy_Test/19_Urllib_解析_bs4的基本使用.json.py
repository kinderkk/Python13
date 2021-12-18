# @Time : 2021/12/18 15:13 
# @Author : 郭帅帅
# @File : 尽量不要使用中文，我是为了方便查看里面内容是什么才用中文的
# @Software: PyCharm

from bs4 import BeautifulSoup

# 通过解析本地文件  来将bs4的基础语法进行讲解
# 默认打开的文件，编码格式是gbk  所以在打开文件时指定编码格式
soup = BeautifulSoup(open('19_Urllib_解析_bs4的基本使用.json.html',encoding='utf-8'),'lxml')


# 根据标签名查找节点
# 找到的是第一个符合条件的数据
# print(soup.a)
# attrs获取标签的属性和属性值
# print(soup.a.attrs)

# bs4 的一些函数
# 1.find
# 返回第一个符合条件的数据
# print(soup.find('a'))
# 根据title的值，找到对应的标签对象
# print(soup.find('a',title="ll"))
# 根据class的值找到对应的标签对象，注意class要加下划线(_)
# print(soup.find('a',class_="aa"))

# 2.find_all
# 返回的是一个列表 并且返回了所有的a标签
# print(soup.find_all('a'))
# 如果想要获取的是多个标签中的数据，那么需要在find_all的参数里 将想要获取的标签放在列表中
# print(soup.find_all(['a','span']))
# print(soup.find_all('li'))

# limit=n 的作用是查找前n个数据
# print(soup.find_all('li',limit=2))

# 3.select(推荐)
# 返回的是一个列表，并且会返回多个数据
# print(soup.select('a'))

# 可以把 . 代表class  类选择器
# print(soup.select('.aa'))

#
# print(soup.select('#l1'))

# 属性选择器 查找到li中有id的标签
# print(soup.select('li[id]'))

# 查找li标签中id为l2的标签
# print(soup.select('li[id="l2"]'))


