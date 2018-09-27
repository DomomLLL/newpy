import urllib.request
import re
qsbk_url = "https://www.qiushibaike.com/pic/page/2/?s=5115845"
user_agent = "Chrome/4.0(compatible; MSIE 5.5; Windows NT)"
req = urllib.request.Request(qsbk_url,headers={'User-Agent':user_agent})
page = urllib.request.urlopen(req)
html = page.read().decode('utf-8')
r1 = r"blank\">\s*<img\ssrc=\"(.*)\"\salt"
a = re.findall(r1,html)
print(a)
count = 0
for i in a:
    count += 1
    urllib.request.retrieve(i,count))
