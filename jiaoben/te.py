import re
import urllib.request 
qsbk_url = "https://www.qiushibaike.com/text/page/2/"
user_agent = "Chrome/4.0(compatible; MSIE 5.5; Windows NT)"
req = urllib.request.Request(qsbk_url,headers={'User-Agent':user_agent})
page = urllib.request.urlopen(req)
html = page.read().decode('utf-8')
rfun = r"<h2>\s+(.+).*<div\sclass=\"content\">\s+.+\s+(.+).*i\sclass=\"number\">(\d+)<"
a = re.findall(rfun,html,re.S)
print(a)

