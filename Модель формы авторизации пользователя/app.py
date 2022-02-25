from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,EmailField
from wtforms.validators import DataRequired
from flask_login import LoginManager
import db_session
from user import User
from flask import Flask, render_template,request,redirect
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    return render_template('login.html', title='Авторизация', form=form)

class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')