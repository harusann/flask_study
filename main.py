from flask import Flask
from src.api.api import api
from src.route import route
import os
from flask_login import LoginManager
from src.module.function import generate_token
from database import create_session, User

app = Flask(__name__, static_folder='static', static_url_path='/')
app.register_blueprint(api)
app.register_blueprint(route)

app.config['SECRET_KEY'] = generate_token(32)

login_manager = LoginManager()
login_manager.init_app(app)
 
 
@login_manager.user_loader
def load_user(user_id):
    session = create_session()
    return session.query(User).filter(User.id == user_id).first()


print(f' * http://localhost:{os.environ.get("FLASK_RUN_PORT")}')