dictone = {}
dictone["shen"] = "cheng"
dictone["zhou"] = "tao"
dictone["li"] = "hua"

print(dictone)

for xin,ming in dictone.items():
    if xin == "shen":
        print("本人来了")
    else:
        print(xin.title()+" "+ming.title())
"""
flag = input("输入int")
while(float(flag)<9.9):
    print( flag+"小于10")
    flag = input("输入int")
"""
def cal(temp1,temp2):
    return int(temp1)+int(temp2)
print(cal('1','2'))