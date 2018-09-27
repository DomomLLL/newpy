from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms import SubmitField
from wtforms.validators import DataRequired, Length, Email
from wtforms.validators import EqualTo

class RegisterForm(FlaskForm) :
	#为了安全要进行表单验证
	name = StringField(label='名字', validators=[DataRequired(), Length(1, 64)])
	email = StringField(label='邮箱', validators=[DataRequired(), Length(1, 128), Email('邮箱好像不对')])
	password = PasswordField(label='密码', validators=[DataRequired(), Length(6, 128)])
	password_again = PasswordField(label='密码', validators=[EqualTo('password', '两次密码不一致，请重新输入')])
	submit = SubmitField(label='提交')
	
