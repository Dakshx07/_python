a1=int(input("enter a number 1 "))
a2=int(input("enter a number 2 "))
a3=int(input("enter a number 3 "))
a4=int(input("enter a number 4 "))

if (a1>=a2) and (a1>=a3) and (a1>=a4):
    print("a1 is the greatest")
elif (a2>=a1) and (a2>=a3) and(a2>=a4):
    print("a2 is the greatest")
elif (a3>=a1) and (a3>=a2) and (a3>=a4):
    print("a3 is the greatest")
else:
    print("a4 is the greatest")
