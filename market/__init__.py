from flask import Flask
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'ladfaldshfakkadshfladshfl'
db = SQLAlchemy(app)

from  market import  routes