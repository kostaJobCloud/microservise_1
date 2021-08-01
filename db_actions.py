
import logging
from flask import jsonify

from app import session
from models import User


class DBUtils(object):

    @staticmethod
    def add_new_user(data):
        logging.info('Adding user has started...')
        new_user = User(first_name=data['first_name'], last_name=data['last_name'], age=data['age'], email=data['email'])
        session.add(new_user)
        session.commit()
        logging.info(f'User {new_user.first_name} {new_user.last_name} has been successfully added to the database.')
        return jsonify({
            'Message': f'User: {new_user.first_name} {new_user.last_name} has been successfully added'
        })

    @staticmethod
    def list_all_users():
        logging.info('Listing all users.')
        users = [
                {
                    'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'age': user.age,
                    'email': user.email
                } for user in session.query(User).all()
                ]
        return jsonify({
            'Users': users
        })

    @staticmethod
    def delete_all_users():
        logging.info('Deleting users process has started.')
        session.query(User).delete()
        session.commit()
        logging.info('All users have deleted.')
        return jsonify({
            'Message': 'All users from the table have been deleted'
        })

    @staticmethod
    def update_user(data, user_id):
        logging.info('Updating user has started.')
        user = session.query(User).get(user_id)
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.email = data['email']
        user.age = data['age']
        session.commit()
        logging.info(f'User {user.first_name} {user.last_name} has successfully updated.')
        return jsonify({
            'Message': f'User {user.first_name} {user.last_name} has successfully updated.'
        })

    @staticmethod
    def get_user(user_id):
        logging.info('Get user from the database.')
        user = session.query(User).get(user_id)
        return jsonify({
            'User': {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'age': user.age
            }
        })

    @staticmethod
    def delete_user(user_id):
        logging.info('Deleting user...')
        session.query(User).filter_by(id=user_id).delete()
        return jsonify({
            'Message': 'User has been deleted successfully'
        })





