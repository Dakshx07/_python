import os

directory_name='/'

contents=os.listdir(directory_name)

for file in contents:
    print(file)