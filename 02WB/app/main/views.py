from flask import render_template,url_for,redirect,request
from flask import abort, flash

from . import main
from app import db

@main.route('/')
def index() :
    #render_template会去app/templates下找模板
    return render_template('main/index.html')

