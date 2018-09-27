#ORM  对象关系映射
#   表---->类
#   记录-->对象

#0.添加数据库配置（参考config.py）
#1.创建sqlarlchmey对象db（用来连接数据库））
#2.构建数据模型类(db.Model，参考app/models.py)
#3.在run.py中导入数据模型类
#4.执行db.create_all()创建表
#  如果表已经存在则不重新创建（即使类修改了也没用）
#  db.drop_all() 删除所有表


from app import db
from app import app
import pymysql
pymysql.install_as_MySQLdb()

from app.models import Student, BTeacher

#根据当前命名空间中的模型类来创建表
db.create_all()

#app.run(debug=True)




