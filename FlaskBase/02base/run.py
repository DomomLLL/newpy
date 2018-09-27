#简单项目架构
#02base
#.
#├── app
#│   ├── __init__.py
#│   ├── static
#│   ├── templates
#│   └── views.py
#└── run.py

#1.在__init__.py中创建flask实例
#from flask import Flask
#app = Flask(__name__)
#from . import views

#2.在views中创建路由和视图函数
#from app import app
#@app.route('/')
#def index() :
#	return 'ok'

#3.在run.py中运行flask实例
from app import app

app.run(debug=True)











