from admin import Admin
from user import User
from database import Database

a = Admin('tiago98', '1234', 3)
u = User('user123', 'abc321')

users = [a, u]
for user in users:
    user.save()

print(Database.find(lambda x: x['username'] == 'tiago98'))
