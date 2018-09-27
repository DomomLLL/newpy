from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms import SubmitField

class RegisterForm(FlaskForm) :
	name = StringField(label='名字')
	password = PasswordField(label='密码')
	password_again = PasswordField(label='密码')
	email = StringField(label='邮箱')
	submit = SubmitField(label='提交')
	
