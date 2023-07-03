from flask import Flask
from route.route import route

app = Flask(__name__, static_folder='static', static_url_path='/')
app.register_blueprint(route)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)