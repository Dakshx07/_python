marks={
    "Daksh":100,
    "rohan":11,
    "Rahul":12,
    "Vijay":13,
    0:'harry'
}

print(marks.items()) # Print all key-value pairs in the dictionary

print(marks.keys())  # Print all keys in the dictionary
print(marks.values())  # Print all values in the dictionary 

marks.update({"Daksh": 99,"rohha":89})  # Update the value for the key "Daksh"
print(marks)  # Print the updated dictionary

print(marks.get("Daksh"))  # Another way to access the value associated with the key "Daksh"

print(marks.get("SHIAK"))  # Print None if the key is not present in the dictionary
print(marks["SHIAK"])  # gives KeyError if the key is not present in the dictionary