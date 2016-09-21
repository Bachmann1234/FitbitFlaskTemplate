import flask_login
import sqlalchemy
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import logout_user, login_required, login_user

from app import db
from app.main.forms import RegistrationForm, LoginForm
from app.models import User
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    if not flask_login.current_user.is_authenticated:
        return redirect(url_for('main.login'))
    return render_template('index.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    status = 200
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.validate(form.password.data):
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid Credentials')
            status = 401
    return render_template('login.html', form=form), status


@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logged Out')
    return redirect(url_for('main.login'))


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    status = 200
    if request.method == 'POST' and form.validate():
        user = User(
            form.username.data,
            form.password.data
        )
        try:
            db.session.add(user)
            db.session.commit()
            flash('Thanks for registering')
            return redirect(url_for('main.login'))
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            flash('Username {} already taken'.format(form.username.data))
            status = 400

    return render_template('register.html', form=form), status
