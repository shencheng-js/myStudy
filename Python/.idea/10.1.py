list = []

for i in range(1,11):

    if(i%2 == 0):
        list.append(i ** 2)
    else:
        list.append(i)

for num in list:
    print(num,end=" ")
print()
list[0] = '10000'


for num in list:
    print(num, end=" ")


print()
del list[0]

for num in list:
    print(num, end=" ")
print()

list.remove(4)
for num in sorted(list):
    print(num, end=" ")

print()
for num in reversed(list):
    print(num, end=" ")

a = list.copy()
for num in a:
    print(num, end=" ")
def cal(temp1,temp2):
    return int(temp1)+int(temp2)