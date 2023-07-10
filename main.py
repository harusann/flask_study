from flask import Flask
from route.api import api
from route.route import route
import os
from dotenv import load_dotenv


app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(route)


load_dotenv()

print(f' * http://localhost:{os.environ.get("FLASK_RUN_PORT")}')