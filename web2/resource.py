from mongoengine import Document, StringField, IntField, BooleanField

class Resource(Document):
    meta = {
        "strict" : False
    }
    name = StringField()
    city = StringField()
    year = IntField()
    height = IntField()
    weight = IntField()
    available = BooleanField(default=False)
