from mongoengine import Document, StringField, ListField


class Questions(Document):
    Category = StringField()
    Type = StringField()
    Difficulty = StringField()
    Question = StringField()
    Correct_answer = StringField()
    Incorrect_answer = ListField()
