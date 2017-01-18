import uuid
from flask import session
from src.common.Database import Database
from src.models import Blog


class User(object):

    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4.hex() if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one('users', {'email ': email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, id):
        data = Database.find_one('users', {'_id': id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(self, email, password):
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password

    @classmethod
    def register(cls, email, password):
        user = cls.get_by_email()
        if user is None:
            new_user = User(email, password)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return False

    @staticmethod
    def login(user_email):
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def get_blogs(self):
        return Blog.find_by_author_id(self._id)

    def json(self):
        return {
            "email": self.email,
            "_id": self._id,
            "password": self.password  # Only being used inside application - not over network
        }

    def save_to_mongo(self):
        Database.insert(collection='users', data=self.json())

