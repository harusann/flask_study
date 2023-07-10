from flask import Flask, request, redirect
from route.api import api
import os
from dotenv import load_dotenv

app = Flask(__name__, static_folder='static', static_url_path='/')
app.register_blueprint(api)

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('./templates/home.html')

@app.route('/', methods=['POST'])
def regist_user():
    print(request)
    return redirect('/templates/success.html')

load_dotenv()

print(f' * http://localhost:{os.environ.get("FLASK_RUN_PORT")}')