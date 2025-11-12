#1 Display message
def display_message():
    print('I am learning about functions in Python.')

display_message() #call the function

#2 Favorite book

def favorite_book(title):
    print(f"One of my favorite books is {title}.")
favorite_book("The Giving Tree")

#3 Function that describes cities and countries

def describe_city(city, country = 'France'):
    print(f"{city} is in {country}.")

describe_city("Paris")

#4 Compares random numbers
import random
def random_compare(user_number):

    random_number = random.randint(1, 100) #Generate a random number between 1 and 100
    if user_number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

random_compare(50) #call function

#5 Modify and display list of names
magician_names = ['Harry Houidini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

show_magicians(magician_names)

def make_great(magicians):
    for i in range(len(magicians)): #gets the total number of items in the list + creates a sequence of index numbers
        magicians[i] = "The Great " + magicians[i]

make_great(magician_names)
show_magicians(magician_names)

#7 Generate a random temperature and provide advice based on the temperature range
import random
def get_random_temp():
    temperature = random.randint(-10, 40)
    return temperature

def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 17 <= temp <= 23:
        print("Nice weather.")
    elif 24 <= temp <= 32:
        print("A bit warm, stay hydrated.")
    elif 33 <= temp <= 40:
        print("It’s really hot! Stay cool.")
main ()