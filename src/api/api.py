from database import User, create_session
from flask import Blueprint, request, jsonify, redirect
from flask import session as client_session
from google.auth import jwt
from flask_login import login_user, login_required, logout_user, current_user


class PostValueError(Exception):
    pass

class MaxValueError(Exception):
    pass


api = Blueprint('login', __name__, url_prefix='/login', static_folder='../../static')


@api.route('/', methods=["POST"])
def create_user():
    session = create_session()
    try:
        # Googleから送られてきたPOSTを辞書型に
        data = request.form.to_dict()
        # デコードをして読み取れる形に
        persed_request = jwt.decode(data['credential'], verify=False)
        name = persed_request['name']
        id = persed_request['sub']
        print(f'name : {name}, id : {id}')
        user = User(name=name, id=id)

        if session.query(User).filter(User.id == id).first() :
            login_user(user)

            print(current_user.name)

            return redirect('/templates/success.html')
        
        else:
            session.add(user)
            session.commit()

            login_user(user)

            return redirect('/templates/success.html')
    
    except PostValueError as e:
        print(e)
        return jsonify({'result':False, 'message':e.args[0]}), 400
    
    except Exception as e :
        print(e)
        return jsonify({'result':False, 'message':'Internal Server Error'}), 500
    
    finally:
        session.close()


@api.route('/get-user')
@login_required
def get_user():
    return jsonify({'id':client_session.get('id')})


@api.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/templates/home.html')