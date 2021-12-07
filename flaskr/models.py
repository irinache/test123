from flask_login import UserMixin
from .db import *

class User(UserMixin):

    def __init__(self, id, username, password, admin):
        self.id = id
        self.username = username
        self.password = password
        self.admin = admin

    @staticmethod
    def get(user_id):
        db = get_db()
        user = db.execute("SELECT * FROM users WHERE id="+str(user_id)).fetchone()
        if user:
            return User(user[0], user[1], user[2], user[3])
        return None

    @staticmethod
    def get_by_credentials(username, password):
        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username='"+username+"' and password='"+password+"'").fetchone()
        if user:
            return User(user[0], user[1], user[2], user[3])
        return None

    def __str__(self):
        return f"<Id: {self.id}, Username: {self.username}, Email: {self.email}>"

    def __repr__(self):
        return self.__str__()

