from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo

class LoginForm(FlaskForm) :
    email = StringField(label='邮箱', validators=[DataRequired(), Email(), Length(6,128)])
    password = PasswordField(label='密码', validators=[DataRequired(), Length(1, 128)])
    remember_me = BooleanField(label='记住我')
    submit = SubmitField(label='登陆')

class RegisterForm(FlaskForm) :
    email = StringField(label='邮箱', validators=[DataRequired(), Email(), Length(6,128)])
    name = StringField(label='昵称', validators=[DataRequired(),  Length(1,128)])
    password = PasswordField(label='密码', validators=[DataRequired(), Length(1, 128)])
    password_agin = PasswordField(label='确认密码', validators=[EqualTo('password','两次输入的密码不一致，请重新输入')])
    submit = SubmitField(label='注册')