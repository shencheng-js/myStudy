voted = {'shen'}
def check_voted(name):
    if voted.get(name):
        print("Let them vote!")
    else:
        voted[name]=True
        print("Let them out")

check_voted('')