s=set()
s.add(20)
s.add(20.0)
s.add("20")

print(s)  # Print the set after adding elements
print(len(s))  # Print the number of elements in the set

# len of s is 2 because 20 and 20.0 are considered the same element in a set