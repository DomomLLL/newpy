from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Student(db.Model) :
    __tablename__='students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), default='zhangsan')
    age = db.Column(db.Integer, default=20)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))

class Teacher(db.Model) :
    __tablename__='teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), default='张三')
    age = db.Column(db.Integer, default=30)
    #lazy='dynamic' 代表访问students的时候返回的是一个query，可以进一步过滤
    #如果没有lazy='dynamic'则访问students的时候返回的是一个列表
    students = db.relationship('Student', backref='teacher', lazy='dynamic')

from flask_login import UserMixin
class User(db.Model, UserMixin) :
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128))
    name = db.Column(db.String(128), default='张三')
    password_hash = db.Column(db.String(128))

    def __str__(self):
        return str(self.id)+":"+self.name

    #构建一个属性
    @property
    def password(self):
        #密码不能读取，如果读取抛出异常
        raise AttributeError('密码不能读取')
    @password.setter
    def password(self, password):
        #利用sha256+杂质串的方式产生hash值
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        #验证密码是否正确
        return check_password_hash(self.password_hash, password)

from . import login_manager
@login_manager.user_loader
def user_load(id) :
    return User.query.get(int(id))


