import os

tutorial_number = input("What Tutorial do want to execute? (#) : ")

files = os.listdir(f'Tutorial{tutorial_number}')

for file_index in range(len(files)): 
    with open(f'Tutorial{tutorial_number}/{files[file_index]}', 'r') as file:
        content = file.read()
        exec(content)

