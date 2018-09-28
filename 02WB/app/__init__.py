#前端框架（JS/Css)
from flask_bootstrap import Bootstrap
#能够把utc时间渲染成当地时间（JS）
from flask_moment import Moment
#邮件
from flask_mail import Mail, Message
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#导入配置字典
from config import config
from flask_login import LoginManager

#变量名字不能变
bootstrap = Bootstrap()
moment = Moment()

#创建login_manager对象
#login_manager通过操作session来控制用户的登陆状态
#通过对session的判断来决定用户能够访问的视图函数
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

mail = Mail()
db = SQLAlchemy()

#提供一个创建app的函数
def create_app(config_name) :
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    moment.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    #在这里可以注册蓝本

    #一个app可以包含多个蓝本，每个蓝本可以分别实现不同的功能
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
