from flask import Flask
from flask_sqlalchemy import SQLAlchemy

##App config
app = Flask(__name__)
app.config['SECRET_KEY'] = '802cd1978a4c4abb76c98c6f99d31305'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

## database
db = SQLAlchemy(app)

from flaskblog import routes