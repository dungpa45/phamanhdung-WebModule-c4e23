import mlab1
from question import Questions

mlab1.connect()

easy = Questions.objects(Difficulty="easy")
medium = Questions.objects(Difficulty="medium")
hard = Questions.objects(Difficulty="hard")

def make_ques(q):

    right = q.Correct_answer
    wrong = q.Incorrect_answer
    wrong.append(right)
    return right,wrong

for e in easy:
    print(e.Question)
    print(e.Type)
    e.Incorrect_answer.append(e.Correct_answer)
    print(e.Incorrect_answer)
