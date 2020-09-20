import unittest 
from test_assert import Anonysurvey

question = "How do you think of our work?"
question1 = Anonysurvey(question)

question1.showQuestion()
print(Anonysurvey.sex)
print("If you want to quit,please press 'q' !")

while True:
    response = input("Please input.")
    if response == 'q' or response == "Q":
        break
    question1.receiveResponse(response)

question1.showResponses()