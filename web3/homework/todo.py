from mongoengine import Document, StringField

class Add_todo(Document):
    name = StringField()
    description = StringField()
    completed = StringField()