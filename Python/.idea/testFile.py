string = ''
with open('E:\\filetset.txt','a') as file:
    lines = file.readlines()

    for content in lines:
        string +=content.rstrip()+" haha "

    file.write("input via python")
print(string)