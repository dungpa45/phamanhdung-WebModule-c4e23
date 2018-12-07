from mongoengine import Document, StringField, IntField, ReferenceField

class Movie(Document):
    title = StringField()
    image = StringField()
    year = IntField()
    user = ReferenceField("User")



