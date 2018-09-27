#!usr/bin/python
print('欢迎进入英雄无敌')
choose = int(input('请选择直接登录（1），或者创建账号（2）：'))
if choose == 2:
    name = input('请输入用户名：')
    passwd = input('请输入密码：')
    print('{},恭喜您注册成功'.format(name))
else:
    name = input('请输入用户名：')
    passwd = input('请输入密码：')
    print('欢迎')
 
