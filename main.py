from flask import Flask, jsonify, session as client_session
from src.api.api import api
from src.route import route
import os
from flask_login import LoginManager
from src.module.function import generate_token
from database import create_session, User
from datetime import timedelta


app = Flask(__name__, static_folder='static', static_url_path='/')
app.register_blueprint(api)
app.register_blueprint(route)

app.config['SECRET_KEY'] = generate_token(32)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'route.default_route'
 
 
@login_manager.user_loader
def load_user(user_id):
    session = create_session()
    return session.query(User).filter(User.id == user_id).first()


@app.before_request
def before_request():
    # リクエストのたびにセッションの寿命を更新する
    client_session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    client_session.modified = True


@login_manager.unauthorized_handler
def unauth_handler():
    return jsonify({
        'result': False,
        'message': 'ログインしていません' 
    }), 400


print(f' * http://localhost:{os.environ.get("FLASK_RUN_PORT")}')