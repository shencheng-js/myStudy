'''path='text_files\guests.txt'
with open(path,'a') as file_object:
    name=input("Please input your name!")
    while name!='p':
        name=input('Please continue input your name!')
        if name!='p':
            file_object.write(name.title())
            print('Hello '+name+'.')
            file_object.write("\n")
        else:
            file_object.write("\n")
            break

            '''

path="text_files/the_reason.txt"
with open(path,'w') as file_object:
    i=1
    reason=''
    while reason!='p':
        reason = input('Please input your reaasons for programming!')
        if reason!='p':
            file_object.write(str(i))
            file_object.write(' ')
            file_object.write(reason.title())
            file_object.write("\n")
            i += 1
        else:
            break

