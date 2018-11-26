from urllib.request import urlopen
import json
from question import Questions
import mlab1

mlab1.connect()

url = "https://opentdb.com/api.php?amount=50"
conn = urlopen(url)

raw_data = conn.read()
page_content = raw_data.decode("utf-8")

dic = json.loads(page_content)

li = dic["results"]

for i in li:
    q=Questions(Category=i["category"], Type=i["type"], Difficulty=i["difficulty"], Question=i["question"], Correct_answer=i["correct_answer"], Incorrect_answer=i["incorrect_answers"])
    q.save()


