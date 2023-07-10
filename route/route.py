from flask import Blueprint, request, redirect

route = Blueprint('route', __name__, url_prefix='/', static_folder='../static', static_url_path='/')

@route.route('/', methods=['GET'])
def index():
    return route.send_static_file('./templates/home.html')

@route.route('/', methods=['POST'])
def regist_user():
    print(request)
    return redirect('/templates/success.html')