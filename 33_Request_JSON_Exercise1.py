import requests
import json
import pprintpp
import random
import html

url = "https://opentdb.com/api.php?amount=1"

endGame = ""
while endGame != "quit":
    r = requests.get(url)
    if (r.status_code != 200):
        endGame = input("Sorry, there was a problem retrieving the question. Press ENTER to try again or type 'quit' to quit the game")
    else:
        answer_number = 1
        data = json.loads(r.text)
        #pprintpp.pprint(data)
        #input("Press Enter to get a new question.")
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)

        print(html.unescape(question) + "\n")

        for answer in answers:
            print(str(answer_number) + "- " + html.unescape(answer))
            answer_number += 1
        input("")



