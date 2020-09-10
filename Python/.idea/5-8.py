'''users=['mao','zhu','zhou','peng','liu','admin']
if users:
    for user in users:
        if user =='admin':
            print('HELLO admin,would you like to see a status report?')
        else:
            print('Hello '+user+',thank you  for logging in again')
else:
    print('SORRY,the users is empty')'''
current_users=['mao','zhu','zhou','peng','liu','admin']
new_users=['mao','nie','he','li','admin']
for new_user in new_users:
    if new_user in current_users:
        print(new_user+",Sorry,your name has been occupied,please input another name")
    else:
        print(new_user+',you name has not been occupied')
