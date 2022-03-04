from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,EmailField
from wtforms.validators import DataRequired
from flask_login import LoginManager
import db_session
from user import User
from flask import Flask, render_template,request,redirect

app = Flask(__name__)
db_session.global_init("dobavlyaem cap/file.db")
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.position = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"

db_sess = db_session.create_session()

db_sess.add(user)
db_sess.commit()