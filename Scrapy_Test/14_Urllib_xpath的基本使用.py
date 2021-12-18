# @Time : 2021/12/18 9:37 
# @Author : 郭帅帅
# @File : 尽量不要使用中文，我是为了方便查看里面内容是什么才用中文的
# @Software: PyCharm

from lxml import etree

# xpath 解析
# 1.本地文件                                        etree.parse
# 2.服务器响应文件  response.read().decode('utf-8')  etree.HTML()

# xpath 解析本地文件
tree = etree.parse("14_Urllib_xpath的基本使用.html")



# tree.xpath('xpath路径')


# 查找ul 下面的li
# li_list = tree.xpath('//ul/li')

# 查找所有有id属性的li标签
# text() 获取标签中的内容
# li_list = tree.xpath('//ul/li[@id]/text()')

# 找到id为l1的li标签
# 注意双引号必须要有
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')

#  查找到id为l1标签的class属性值
# li = tree.xpath('//ul/li[@id="l1"]/@class')

# 查询id包含l 的li标签
# li_list = tree.xpath('//ul/li[contains(@id,"l")]/text()')

# 查询id的值 以l开头的li标签
# li_list = tree.xpath('//ul/li[starts-with(@id,"c")]/text()')

# 查询id为l1 和 class为a1
# li_list = tree.xpath('//ul/li[@id="l1" and @class="a1"]/text()')


li_list = tree.xpath('//ul/li[@id="l1"]  | //ul/li[@id="l2"]')

# 判断列表的长度
print(li_list)
print(len(li_list))
