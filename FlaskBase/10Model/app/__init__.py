from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['WTF_CSRF_ENABLE'] = True

app.config.from_object('config')

#构建一个访问数据库的对象（会与数据库建立连接，所以必须放到app配置之后)
db = SQLAlchemy(app)

from . import views
