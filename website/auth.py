from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully.', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect, please try again.', category='error')
        else:
            flash('Username does not exist', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirmpassword = request.form.get('confirmPassword')

        user = User.query.filter_by(username=username).first()

        if user:
            flash('This user already exists.', category='error')
            return redirect(url_for('views.login'))

        elif len(username) < 4:
            flash("Username must be longer than 4 characters.", category='error')
        elif password != confirmpassword:
            flash("Passwords do not match.", category='error')
        elif len(password) < 6:
            flash("Password length must be more than 6 characters.", category='error')
        else:
            new_user = User(username=username, password=generate_password_hash(password, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created successfully!", category='success')
            return redirect(url_for('views.home'))
        
    return render_template("sign_up.html", user=current_user)


