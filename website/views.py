from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/login')
def login():
    return render_template("login.html")

@views.route('/signup')
def signup():
    return render_template("sign_up.html")



