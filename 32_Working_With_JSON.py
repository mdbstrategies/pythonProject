#https://opentdb.com/api.php?amount=5&category=22&difficulty=medium&type=multiple

import requests

r = requests.get("https://opentdb.com/api.php?amount=5&category=22&difficulty=medium&type=multiple")
var = r.status_code
var1 = r.text

import json
question = json.loads(r.text)

#print(question)


import pprintpp
#pprintpp.pprint(question)
print(question['results'][0]['category'])
print(question['results'][0]['incorrect_answers'])

person = {'Name': 'John', 'Age': 30}
person_json = json.dumps(person)
print(person_json)