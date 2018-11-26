print("Learn how to convert string to dictionary using json library.")
print("A: import json and use json.loads(your string)")

import json

valid_json_string = '{"name":"Jonh","age":30}'  
data = json.loads(valid_json_string)
print(data)
