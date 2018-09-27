#1.导入flask
from flask import Flask

#2.构建flask对象
#flask对象中有socket，能有与浏览器建立连接
#能够接收浏览器的数据，并且能够发送数据给浏览器
#浏览器和web服务器之间的数据符合http协议
#flask对象能够解决http协议
app = Flask(__name__)

#3.定义视图函数并添加路由
@app.route('/abc')
def index() :
	return 'hello flask'

@app.route('/')
def root() :
	return '''
		<h1>这是一个大标题</h1>
		<p>这是一个段落</p>
'''

#如何渲染前端工程师写好的页面
#a.在test.py同级目录下创建templates和static文件夹
#b.把 *.html文件 放到templates文件夹
#c.把 其他文件夹 放到static文件夹
#d.构建一个视图函数并且添加一个路由
#e.替换css js images的路径

#把css/替换为/static/css/
#:%s/css\//\/static\/css\//g

from flask import render_template
@app.route('/bp')
def bp() :
	#把index.html的内容读出来做成字符串，然后返回
	#注意：render_template默认去templates文件夹下找index.html
	return render_template('index.html')

@app.route('/add/<int:a>/<int:b>')
def add(a, b) :
	return str(a + b)

#静态路由优先
@app.route('/add/1/2')
def hello() :
	return 'ok'

#4.运行flask
app.run(debug=True)

        






