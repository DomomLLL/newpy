from flask import Flask

app = Flask(__name__)

app.config.from_object('config')

print(app.config['ABC'])

from . import views
