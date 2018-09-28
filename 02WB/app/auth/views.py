from . import auth
from flask import render_template
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm,RegisterForm
from flask import abort
from app.models import User
from flask import redirect, flash, url_for
from app import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user is None:
            abort(404)
        if user.check_password(password):
            login_user(user, form.remember_me.data)
            return redirect(url_for('.user_info'))
        else:
            flash('邮箱或者密码错误')
            return redirect(url_for('.login'))
    return render_template('auth/login.html', form=form)


@auth.route('/user_info')
@login_required
def user_info():
    return render_template('auth/user_info.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))

@auth.route('/register',methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        u = User()
        u.name = form.name.data
        u.email = form.email.data
        u.password = form.password.data
        j = User.query.filter_by(email = u.email).first()
        if j is not None:
            flash("邮箱已经被注册")
            return redirect(url_for('.register'))
        db.session.add(u)
        db.session.commit()
        flash('注册成功！请登录')
        return redirect(url_for('.login'))
    return render_template('auth/register.html',form = form)

