#usr/bin/python
x=int(input("请输入年份:"))
a = int(4)
c=x%a
if(c>0):
    print(x,"年有366天")
else:
    print(x,"年有365天")

