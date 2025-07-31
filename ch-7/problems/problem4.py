n=int(input("enter a number "))
sum=0

# for i in range(1,n+1):
#     sum += i

# print(f"The sum of numbers from 1 to 10 is: {sum}")  # Print the sum of numbers from 1 to 10


i=1
while(i<=n):
    sum += i
    i += 1

print(f"The sum of numbers from 1 to {n} is: {sum}")  # Print the sum of numbers from 1 to n