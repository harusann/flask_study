from flask import Blueprint, request, redirect
from flask_login import LoginManager
from google.auth import jwt
import secrets

static_url = secrets.token_urlsafe(16)

route = Blueprint(
    'route', __name__, 
    url_prefix='/', 
    static_folder='../static',
    static_url_path='/'
    )


@route.route('/', methods=['GET', 'POST'])
def default_route():

    # GET のアクセスなら
    if request.method == 'GET':
        return route.send_static_file('templates/home.html')


    # POST のアクセスなら
    if request.method == 'POST':
        # Googleから送られてきたPOSTを辞書型に
        data = request.form.to_dict()
        # デコードをして読み取れる形に
        decoded_data = jwt.decode(data['credential'], verify=False)
        print(decoded_data)

        return route.send_static_file('templates/success.html')


@route.route('/login_faild')
def login_faild() :
    return route.send_static_file('templates/loginFaild.html')