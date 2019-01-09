from saveable import Saveable


class User(Saveable):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'

    def login(self):
        return f'{self.username} logged in'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password
        }
