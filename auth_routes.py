from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
from app.models import db, Utilisateur

auth_bp = Blueprint('auth', __name__)

from flask import redirect, url_for

@auth_bp.route('/')
def home():
    return redirect(url_for('auth.login'))


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        utilisateur = Utilisateur.query.filter_by(email=email).first()

        if utilisateur and bcrypt.check_password_hash(utilisateur.mot_de_passe, password):
            login_user(utilisateur)
            return redirect(url_for('equipe.welcome'))  # بدلها بالصفحة المناسبة
        else:
            flash('Email ou mot de passe incorrect', 'danger')

        if utilisateur.role == 'admin':
            return redirect(url_for('admin.dashboard'))
            


    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
