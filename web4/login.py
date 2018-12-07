from mongoengine import Document, StringField

class Login(Document):
    username = StringField()
    password = StringField()
    