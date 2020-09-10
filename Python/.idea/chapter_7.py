'''name=input("Please input your name:")
print("\nHello "+name+"!")

'''

height=input("How tall are you,in centimeter?")
height=int(height)

if height>=180:
    print("You are tall enough to ride!")
elif height>=170 and height<180:
    print("You can ride,but please be careful")
else:
    print("you can not attend!")
