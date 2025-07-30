a=int(input("enter a number "))

if (a>18):
    print("you are  eligible to vote")
elif(a<0):
    print("you have entered a negative number, please enter a valid age")
else:
    print("you are not  eligible to vote")