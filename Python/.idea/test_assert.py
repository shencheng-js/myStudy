class Anonysurvey():
    sex = 1
    def __init__(self,question):
        self.question = question
        self.responses = []

    def receiveResponse(self,response):
        self.responses.append(response)

    def showQuestion(self):
        print(self.question)

    def showResponses(self):
        for response in self.responses:
            print("-"+response)


