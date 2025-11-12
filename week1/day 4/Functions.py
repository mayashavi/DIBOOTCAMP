#Functions: sequence of commands that can be reused
#FUNCTIONS:

#syntax of a function:

#def <name_of_function>(empty/<arguments>):
#   an indented block of code 

#call the function by the name of it
def greetings():
    print('Welcome, user!')

greetings()

#arguments in Functions
def greetings(user_name):
    print(f'Welcome, {user_name}!')

greetings('Maya')

#default arguments in Functions
def greetings(user_name = 'John Doe'):
    print(f'Welcome, {user_name}!')

greetings('')

# positional argument = the position in which you enter the arguments matter
def greetings(user_name, language='EN'):
    if language == 'EN':
        print(f'Welcome, {user_name}')
    elif language == 'PT':
        print(f'Bem-vindo, {user_name}')
    elif language == 'IT':
        print(f'Benvenuto, {user_name}')
    elif language == 'SP':
        print(f'Bienvenido, {user_name}')
    else:
        print(f'Hello, {user_name}')

greetings('Maya')

#keyword arguments
def greetings(user_name, language='EN'):
    if language == 'EN':
        print(f'Welcome, {user_name}')
    elif language == 'PT':
        print(f'Bem-vindo, {user_name}')
    elif language == 'IT':
        print(f'Benvenuto, {user_name}')
    elif language == 'SP':
        print(f'Bienvenido, {user_name}')
    
greetings(language = 'JP', user_name = 'Maya')

# create a function called country_info that receives a country name as argument
# and prints the capital of that country. Make the country name argument default
# Naboo (star wars planet). Its capital is Theed

#def country_info(country='Naboo'):
   # if country == 'Russia':
       # print(f'Moscow')
  #  elif country == 'France':
   #     print(f'Paris')
   # elif country == 'Peru':
   #     print(f'Lima')
   # elif  country == 'Naboo':
  #      print(f'Theed')
    
def country_info(country='Naboo'):
    if country == 'Russia':
       capital = 'Moscow'
    elif country == 'France':
        capital = 'Paris'
    elif country == 'Peru':
        capital = 'Lima'
    elif  country == 'Naboo':
        capital = 'Theed'
    return capital
print(country_info('Russia'))

def sum_numbers(x, y):
    result = x + y
    return result

def multiply(j):
    multiplier = sum_numbers(3, 2)
    result = j * multiplier
    return result

print(multiply(4))

#using the return keyword