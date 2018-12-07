import mlab
from models.user import User

mlab.connect()
# User(username="admin1",password="321").save()
# User(username="admin2",password="456").save()
# User(username="admin3",password="789").save()

for user in User.objects():
    print(user.username,user.password)
