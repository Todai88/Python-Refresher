from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user

from . import users_blueprint

"""
TODO:
    Add non-imported dependencies.
"""
from .forms import RegisterForm, LoginForm
from app.models import User
from app import db

"""
Routes
"""


@users_blueprint.route('/profile')
@login_required
def profile():
    return render_template('users/profile.html')


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    """
    Registers a user if not logged in or
    redirects the logged in user the profile page.
    :return:
    """

    if current_user.is_authenticated:
        flash('Already registered! Redirecting you to your Profile page')
        return redirect(url_for('users.profile'))

    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user = User(form.email.data, form.password.data)
        new_user.authenticated = True
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash('Registered, {}'.format(new_user.email))
        return redirect(url_for('users.profile'))
    return render_template('users/register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Already logged in! Redirecting to your profile page')
        return redirect(url_for('users.profile'))

    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.is_correct_password(form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=form.remember_me.data)
                flash('Logging in, {}'.format(current_user.email))
                return redirect(url_for('users.profile'))
        flash('Error: incorrect user credentials.')
    return render_template('users/login.html', form=form)


@users_blueprint.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    flash('Logged out')
    return redirect(url_for('recipes.index'))
