# @Time : 2021/12/18 12:26 
# @Author : 郭帅帅
# @File : 尽量不要使用中文，我是为了方便查看里面内容是什么才用中文的
# @Software: PyCharm
import json
import jsonpath

obj = json.load(open('17_Urllib_解析jsonPath.json','r',encoding='utf-8'))

# 书店所有书的作者
# author_list = jsonpath.jsonpath(obj,'$.store.book[*].author')
# print(author_list)


# 所有的作者
# author_list = jsonpath.jsonpath(obj,'$..author')
# print(author_list)

# store 下面的所有的元素
tag_list = jsonpath.jsonpath(obj,'$.store.*')
print(tag_list)

# 最后一本书
