userInp = input("something:\n").split(' ')

userInp[0] = int(userInp[0])

userInp[2] = int(userInp[2])
if userInp[1] == '+':
     print(userInp[0] + userInp[2])
elif userInp[1] == '*':
     print(userInp[0] * userInp[2])
elif userInp[1] == '-':
     print(userInp[0] - userInp[2])
elif userInp[1] == '/':
     print(userInp[0] / userInp[2])