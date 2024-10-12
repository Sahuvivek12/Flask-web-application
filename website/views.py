from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from .models import User, db, Note

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Length of the note is too short.', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note created successfully!', category='success')

    user_notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template("home.html", user=current_user, notes=user_notes)

@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash("Login successful!", category='success')
            return redirect(url_for('views.home'))
        else:
            flash("Invalid username or password.", category='error')

    return render_template("login.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note_id = request.json.get('noteId')
    note = Note.query.get(note_id)

    if note and note.user_id == current_user.id:  
        db.session.delete(note)
        db.session.commit()
        flash('Note deleted successfully!', category='success')
    else:
        flash('Note not found or you do not have permission to delete it.', category='error')

    return {}, 204 
