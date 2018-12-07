from mongoengine import Document, StringField

class User(Document):
    username = StringField()
    password = StringField()

#Test
# de an noi dung trong file import
if __name__ == "__main__":
    print("user--")