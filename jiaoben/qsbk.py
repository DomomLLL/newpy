import urllib.request
import re
count = int(input('请输入查看多少页：'))
h = 1
for i in range(count):
    h += 1
    qsbk_url = "https://www.qiushibaike.com/text/page/{}/".format(h)
    user_agent = "Chrome/4.0(compatible; MSIE 5.5; Windows NT)"
    req = urllib.request.Request(qsbk_url,headers={'User-Agent':user_agent})
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    rfun = r"<div\sclass=\"content\">\s+.+\s+(.+)"
    r1 = r"i\sclass=\"number\">(\d+)<"
    r2 = r"<h2>\s+(.+)"
    a = re.findall(rfun,html)
    b = re.findall(r1,html)
    c = re.findall(r2,html)
    print(a)
    print(b)
    print(c)

