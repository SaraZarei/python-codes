userInpList = input("please enter something:\n").split(',')
quest = input("please say a, d or r:\n")

if quest == 'a':
    userInpList.sort()
elif quest == 'd':
    userInpList.sort(reverse = True)
elif quest == 'r':
     userInpList.reverse()
else:
    print("your command is unknown to me!!!")
print(','.join(userInpList))