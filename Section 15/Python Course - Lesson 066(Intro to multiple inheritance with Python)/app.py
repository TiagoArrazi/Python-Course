from admin import Admin
from database import Database

a = Admin('tiago', '1234', 3)
a.save()
print(Database.find(lambda x: x['username'] == 'tiago'))
