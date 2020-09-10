
'''
def display_message(pet_name,pet='dog'):
    print("\nI have a "+pet+".")
    print("My "+pet+"'s name is "+pet_name.title()+'.')


display_message('banana')

#默认值
def make_shirt(size="big",character='I love Python.'):
    print("Hello,your "+size+" shirt's character is "+character+".")


make_shirt('medium','Apple')

#返回值
def formatted_name(first_name,last_name,medium_name=' '):
    if medium_name:
        full_name = first_name +' '+ medium_name +' '+ last_name
    else:
        full_name=first_name+' '+last_name
    return full_name.title()

musician = formatted_name('shen','cheng','yu')
print(musician)

#测试副本
musicians=['mao','zhu','zhou','liu']
anothermusicians=musicians[:]
print(anothermusicians)
print(musicians)
print("\n")
musicians[0]='he'
print(anothermusicians)
print(musicians)
'''

def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+
          "-inch pizza with the following toppings" )
    for topping in toppings:
        print(" -"+topping)