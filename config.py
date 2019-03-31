from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import datetime
import re

app = Flask(__name__)
# configurations to tell our app about the database we'll be connecting to
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tweets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# an instance of the ORM
db = SQLAlchemy(app)
# a tool for allowing migrations/creation of tables
migrate = Migrate(app, db)
app.secret_key="secret#key#is#set"
bcrypt = Bcrypt(app)
