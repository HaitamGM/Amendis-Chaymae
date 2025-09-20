from flask import Blueprint, render_template
from flask_login import login_required

equipe_bp = Blueprint('equipe', __name__)

@equipe_bp.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')  # fichier HTML li 3andk f templates
