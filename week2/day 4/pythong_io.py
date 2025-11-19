#PYTHON - I/O
#OLD-SCHOOL WAY: you need to close file after using it - USING CLOSE() METHOD
file_obj = open('file-name.txt', 'w') #'w' = is for writing
#your code to do anything you want
file_obj.close()

#NEW WAY: use with statement
with open('secrets.txt', 'r') as file_obj: #
    print(file_obj.read())

#solution for the FileNotFoundError:
dir_path = os.path.dirname(os.path.realpath(__file__))
