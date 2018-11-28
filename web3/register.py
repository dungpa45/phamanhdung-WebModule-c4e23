from mongoengine import Document, StringField, IntField,BooleanField


class Register(Document):
    username = StringField()
    email = StringField()
    email_verified = BooleanField(default=False)
    password = StringField()
