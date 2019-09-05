from urllib.request import urlopen as ur, urlopen
from lxml import etree as et
import time
import json
import sys
from lxml.doctestcompare import strip

last_twitter_content = []
# 第一步， 模拟发起请求
url = "https://twitter.com/search?vertical=news&q=lang%3A"+sys.argv[1]+"&src=typd"
print(url)
response = urlopen(url)

# 第二步，  得到结果 : 源码
html_content = response.read().decode("UTF-8")


#  第三步， 如何处理数据
tree = et.HTML(html_content)
print(tree)

# //*[@id="articleslist-wrapper"]/ul/li/p/text()  content
# //*[@id="articleslist-wrapper"]/ul/li/a/p  title
spans = tree.xpath('//*/div/div/div/p')
print(type(spans))
for span in spans:
    print(span,span.text)
    last_twitter_content.append(span.text)

with open(file="/home/zhangzhongfang/python/data/"+sys.argv[1]+"_"+str(sys.argv[2])+"_twitter.txt", mode="w") as f:
    for india_twitter in last_twitter_content:
        f.write(india_twitter)
        f.write("\n")
    time.sleep(5)