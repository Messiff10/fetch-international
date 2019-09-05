from urllib.request import urlopen as ur, urlopen
from lxml import etree as et
import time
import json

from lxml.doctestcompare import strip

last_india = []
last_india_title = []
last_india_content = []
# 第一步， 模拟发起请求
url = "https://www.khaskhabar.com/features"
response = urlopen(url)

# 第二步，  得到结果 : 源码
html_content = response.read().decode("UTF-8")


#  第三步， 如何处理数据
tree = et.HTML(html_content)

# //*[@id="articleslist-wrapper"]/ul/li/p/text()  content
# //*[@id="articleslist-wrapper"]/ul/li/a/p  title
spans = tree.xpath('//*[@id="articleslist-wrapper"]/ul/li')
for span in spans:
    titles = span.xpath('./a/p')
    last_india_title.append("\t".join([strip(t.text) for t in titles]))
    contents = span.xpath('./p/text()')
    last_india_content.append("\t".join([strip(t[:-3]) for t in contents]))

for i in range(0,len(last_india_content)):
    title = last_india_title[i]
    if title.endswith("..."):
        title = title[:-3]
    if (i==len(last_india_content)):
        content = last_india_content[i][:-1]
    content = last_india_content[i]
    last_india.append(",".join([title,content]))

with open(file="/home/hadoop/zzf/python/data/pi_IN.txt", mode="w") as f:
    for india in last_india:
        f.write(india)
        f.write("\n")
    time.sleep(5)