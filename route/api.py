from database import User, create_session
from flask import Blueprint, request, jsonify
import json

class PostValueError(Exception):
    pass

class MaxValueError(Exception):
    pass

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/get-user')
def get_user():

    session = create_session()

    try:
        users = session.query(User).all()
        return jsonify([user.to_dict() for user in users]), 300
    
    except Exception as e:
        print(e)
        return jsonify([]), 500
    
    finally:
        session.close()


@api.route('/create-user', methods=["POST"])
def create_user():
    session = create_session()
    point = 0
    try:
        persed_request = json.loads(request.data)
        name = persed_request['name']
        email = persed_request['email']

        print(f'name : {name}, email : {email}')

        if (email == None or email == '') or (name == None or name == ''):
            raise PostValueError('メールアドレスと名前を入力してください')

        if session.query(User).filter(User.email == email).first() :
            raise PostValueError('登録済みのメールアドレスです')

        user = User(name=name, email=email)
        session.add(user)
        session.commit()

        return jsonify({'result':True}), 200
    
    except PostValueError as e:
        print(e)
        return jsonify({'result':False, 'message':e.args[0]}), 400
    
    except Exception as e :
        print(e)
        print(f'point : {point}')
        return jsonify({'result':False, 'message':'Internal Server Error'}), 500
    
    finally:
        session.close()