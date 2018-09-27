from app import app
from flask import render_template,url_for,redirect,flash

@app.route('/')
def index() :
	return render_template('index.html')

@app.route('/students')
def students() :
	return render_template('students.html')

@app.route('/teachers')
def teachers() :
	return render_template('teachers.html')

@app.route('/add_teacher')
def add_teacher() :
	return render_template('add_teacher.html')

@app.route('/add_student')
def add_student() :
	return render_template('add_student.html')
