from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = 'auth.login'

    from .models import Utilisateur  # تأكد بالاستيراد هنا

    @login_manager.user_loader
    def load_user(user_id):
        return Utilisateur.query.get(int(user_id))

    from .routes import auth_bp, equipe_bp, admin_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(equipe_bp, url_prefix='/equipe')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app

