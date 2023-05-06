from app import app
from flaskext.mysql import MySQL # By using this we can use mysql database

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'sqluser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'rest_api'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)