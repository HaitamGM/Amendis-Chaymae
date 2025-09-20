from flask import Blueprint, render_template
from flask_login import login_required

equipe_bp = Blueprint('equipe', __name__, url_prefix='/equipe')

@equipe_bp.route('/welcome')
@login_required
def welcome():
    return render_template('employee.html')
