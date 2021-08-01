import logging

from flask import Flask, request, Blueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from decorators import error_handler

logging.basicConfig(level=logging.INFO)
logging.info('Application has started.')

engine = create_engine('postgresql://kosta:kosta@localhost:5432/my_db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

user_routes = Blueprint('user_routes', __name__)
app.register_blueprint(user_routes)


@app.route('/', methods=['GET'])
@error_handler
def get_users():
    from db_actions import DBUtils
    response = DBUtils.list_all_users()
    session.close()
    return response


@app.route('/user', methods=['POST'])
@error_handler
def add_user():
    from db_actions import DBUtils
    data = request.get_json()
    response = DBUtils.add_new_user(data)
    session.close()
    return response


@app.route('/user/<id>', methods=['PUT'])
@error_handler
def update_user(id):
    from db_actions import DBUtils
    data = request.get_json()
    response = DBUtils.update_user(data, id)
    session.close()
    return response

@app.route('/user/<id>', methods=['GET'])
@error_handler
def get_user(id):
    from db_actions import DBUtils
    response = DBUtils.get_user(id)
    session.close()
    return response

@app.route('/user/<id>/delete', methods=['DELETE'])
@error_handler
def delete_user(id):
    from db_actions import DBUtils
    response = DBUtils.delete_user(id)
    session.close()
    return response


@app.route('/users/delete', methods=['DELETE'])
@error_handler
def delete_users():
    from db_actions import DBUtils
    if request.method == "DELETE":
        return DBUtils.delete_all_users()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    logging.info('Application stops working.')
