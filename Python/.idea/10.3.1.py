#尝试try
'''try:
    print(5/0)
except ZeroDivisionError:
    print("你正在除0")
#除法计算
print("please input two numbers.")
print("input 'q' to stop!")
while True:
    first_number=input("\nPlease input the first number!")
    if first_number=='q':
        break
    second_number=input("\nPlease input the second number!")
    if second_number=='q':
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("你正在除0")
    else:
        print(answer)



def count_world(filename):
    try:
        with open(filename) as object_text:
            contents=object_text.read()
    except FileNotFoundError:
        #msg="Sorry,the file path "+filename+" does not exist."
        #print(msg)
        pass

    else:
        words=contents.split()
        lens=len(words)
        print("The text contents "+str(lens)+" words")

count_world("text_files/Th Wonderful Year.txt")     '''
'''import json
#numbers=[1,2,3,4,5,6]
filename="usernames.json"
with open(filename) as f_obj:
    numbers = json.load(f_obj)
#    json.dump(numbers,f_obj)
print(numbers)




import json
def gree_users():
    filename="usernames.json"
    try:
        with open(filename) as f_obj:
            name=json.load(f_obj)
    except FileNotFoundError:
        name=input("Please input your name,and I will remmember you when youcome back.")
        with open(filename,'w') as f_obj:
            json.dump(name,f_obj)
    else:
        print("Welcome back "+name)

gree_users()
'''

import json
def find_username():
    filename="usernames.json"
    try:
        with open(filename) as f_obj:
            name=json.load(f_obj)
    except FileNotFoundError:
        return None
    else :
        return name

def input_username():
    filename="username.json"
    name = input("请输入您的名字，我们会记住您的名字。")
    with open(filename,'w') as f_obj:
        json.dump(name,f_obj)
    return name

def greet_user():
    usernames=find_username()
    if usernames:
        print("Welcome back "+usernames+".")
    else:
        input_username()

greet_user()