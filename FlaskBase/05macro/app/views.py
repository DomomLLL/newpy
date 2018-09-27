from flask import render_template
from app import app

@app.route('/')
def index() :

	t1 = {'name':'张三', 'age':20, 'sex':1}
	t2 = {'name':'张四', 'age':21, 'sex':2}
	t3 = {'name':'张无', 'age':22, 'sex':2}
	t4 = {'name':'张刘', 'age':23, 'sex':1}
	return render_template('index.html', slist=[t1,t2,t3,t4])
