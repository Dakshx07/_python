num=int(input("enter a number "))

product = 1
for i in range(1, num + 1):
    product *= i  # Calculate factorial by multiplying numbers from 1 to n

print(f"factorial of {num} is: {product}")  # Print the factorial of the given number