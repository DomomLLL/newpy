import urllib.request
import re
x= int(input("请输入页数:"))
y = 1
for j in range(x):
    y += 1
    qsbk_url = "https://www.qiushibaike.com/pic/page/{}/?s=5115845".format(y)
    user_agent = "Chrome/4.0(compatible; MSIE 5.5; Windows NT)"
    req = urllib.request.Request(qsbk_url,headers={'User-Agent':user_agent})
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    r1 = r"blank\">\s*<img\ssrc=\"(.*)\"\salt"
    r2 = r"blank\">\s*<img\ssrc=\".*\"\salt=\"(.*)\""
    a = re.findall(r1,html)
    b = re.findall(r2,html)
    print(a)
    print(b)
    count = 0
    for i in a:
        kk = 'https:'
        urllib.request.urlretrieve(kk+i,'{}.jpg'.format(b[count]))
        count += 1
