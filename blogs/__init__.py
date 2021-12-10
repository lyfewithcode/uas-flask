from flask import Flask
from flaskext.mysql import MySQL
from blogs.mysql_env import *

app = Flask(__name__)

# setting mysql
mysql = MySQL()
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
app.config['MYSQL_DATABASE_USER'] = db_user
app.config['MYSQL_DATABASE_PASSWORD'] = db_password
app.config['MYSQL_DATABASE_DB'] = db_name
app.config['MYSQL_DATABASE_HOST'] = db_host
mysql.init_app(app)
conn = mysql.connect()

from blogs import routes
