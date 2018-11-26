import mlab1
from question import Questions

mlab1.connect()

easy = Questions.objects(Difficulty="easy")
medium = Questions.objects(Difficulty="medium")
hard = Questions.objects(Difficulty="hard")

print(easy)