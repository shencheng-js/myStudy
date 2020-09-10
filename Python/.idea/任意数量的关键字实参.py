'''def build_profile(first,last,**user_info):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('shen','cheng',location='chong_qing',country='China')
print(user_profile)'''
import 函数

from 函数 import *

make_pizza(18,'apple','banana','orange')

def pizza_making(things):
    print("The pizza contains the next things:")
    for thing in things:
        print("-"+thing)
things=[]
print("Please input the things youwant to attend to the pizza.(press 'q' to stop)")
flag=" "
while flag!='q':
    flag=input()
    if flag !='q':
        things.append(flag)
    else:
        break
pizza_making(things)