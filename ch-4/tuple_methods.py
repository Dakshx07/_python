b=(12,11,"da","sddfs","sdw",113,False,113,212.1)   #tuple are immutable

num=b.count(113)  # count the number of occurences of the element in the tuple
print(num)

idx=b.index(113)  # find the index of the element in the tuple
print(idx)

b=b*2  # multiply the tuple by a scalar it will repeat the tuple
print(b)

print(113 in b)  # check if the element is present in the tuple or not
print(113 not in b)  # check if the element is not present in the tuple
 


