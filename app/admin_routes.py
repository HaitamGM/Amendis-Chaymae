from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'admin':
        flash('You do not have permission to access this page.', 'danger')
        return "Access Denied", 403
    return render_template('dashboard.html')
