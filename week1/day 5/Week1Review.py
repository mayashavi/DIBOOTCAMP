#VOCAB Words:
#Basic Data Types: Floats, Integers, Strings, Booleans, NoneType
#Variables: how to assign a value to a variable - memory location
#Conditionals: if statements
#Complex Data: Lists, Tuples, and, Sets (ordered structures, have indexes, iterable [can be looped])
#Loops: for & while
#Dictionaries: more complex - "label" the data
#range(): creates a sequence of integers, starting from a beginning number, ending before an ending number ('step')
#enumerate(): takes an iterable (like a list, tuple, or string) and returns pairs (index, item)
#Functions
#Local and Global Scope
#*ARGS and **KWARGS


# - EVERYTHING IN PYTHON ARE OBJECTS - 
# - STRINGS ARE IMUTABLE SEQUENCES OF CHARACTERS -

#LIST = Mutable, ordered sequence

friends = ['Ross', 'Rachel', 'Monica', 'Joey','Chandler', 'Phoebe']
print(friends[0]) #Ross
print(friends[2:5]) #Monica-Chandler (slicing)

#LIST Methods
friends.append('Janice') #Adds to the end
print(friends)
friends.insert(2, 'Janice') #Inserts and changes order & then remove 
#print(friends)
friends.remove('Monica')
print(friends)

popped_value = friends.pop(-2) #pop with no info deletes last element
print(f'bye bye {popped_value}') #Removes at index and does something

#sorted() /// alphabetical / smallest to largest
# print(friends)
# sorted_friends = sorted(friends)

#sort()
print(friends)
friends.sort()
print(friends)

# user_info = input('enter your name & age seperated by comma: ').split(',') #by space, comma, hyphen
# print(user_info)
#split() - creates a list as output

#join(): is a string method in Python that combines elements of a list into one string, placing a separator between each element.
students = input('enter student names').split()

print(f"The new students are: {', '.join(students)}")

#LOOPS
# FOR LOOP
#syntax:
#for <variable> in <sequence>:
#   an indented line of code

for student_name in students:
    print(f'Welcome, {student_name}')

#WHILE LOOP

toppings_list = []
price = 10

while True:
 topping = input('enter the toppings or "q" for quit: ').lower()
 if topping == 'q':
    print(f'Your toppings are: {', '.join(toppings_list)} and the price is {price}')
    break

topping.append(topping)
price +- 2.5
print(f'the {topping} was added to your pizza')

#D2/BOARD:
board = [['_','_','_',
          '_','_','_',
          '_','_','_',]]
board[0][1] = 'x'
print(board)

def print_board(board):
    print('*'*17) #print 17 stars
    print(f'*    {board[0][0]}|{board[0][1]}|{board[0][2]}    *')
    print('*    __|__|__    *')

print(board)

   
