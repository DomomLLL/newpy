from app import app
from flask import render_template

@app.route('/')
def index() :
	return render_template('index.html', title='自我介绍', name='张三', work='我是一个唱戏的')

@app.route('/a')
def a() :
	return render_template('index.html', title='自我介绍', name='李斯', work='我是一个好人')

@app.route('/student')
def student() :
	s_list = ['张三', '李斯', '王无', '章六']	
	return render_template('student.html', slist=s_list)

@app.route('/teacher')
def teacher() :
	t_dic = {'name':'zhangsan', 'age':35, 'sex':1}	
	return render_template('teacher.html', t=t_dic)	

@app.route('/teachers') 
def teachers() :
	t1 = {'name':'zhangsan', 'age':32, 'sex':1}
	t2 = {'name':'lisi', 'age':33, 'sex':0}
	t3 = {'name':'wangwu', 'age':34, 'sex':0}
	t4 = {'name':'sunliu', 'age':36, 'sex':1}
	t_list = [t1,t2,t3,t4]
	return render_template('teachers.html', tlist=t_list)	







