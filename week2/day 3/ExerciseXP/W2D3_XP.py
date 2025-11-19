#Using the code above, implement the relevant methods and dunder methods which will output the results below.
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    # String representation
    def __str__(self):
        if self.amount == 1:
            return f"{self.amount} {self.currency}"
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return self.__str__()

    # Allow int(c1)
    def __int__(self):
        return self.amount

    # Addition with int or Currency
    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other

        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type {self.currency} and {other.currency}."
                )
            return self.amount + other.amount

        return 

    # In-place addition: c1 += x
    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
            return self

        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            self.amount += other.amount
            return self

        return 

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#the comment is the expected output
print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

#print(c1 + c3)

#Create a func.py file with a function that sums two numbers and prints the result. Then, import and call the function from exercise_one.py.
from functionxxp import add_numbers
add_numbers(5, 7)

#Random String of Length 5
import string
import random

def random_string():
    letters = string.ascii_letters  # a–z + A–Z
    result = ""

    for _ in range(5):
        result += random.choice(letters)

    return result

print(random_string())

#Current Date
import datetime

def display_current_date():
    today = datetime.date.today()
    print("Today's date is:", today)

display_current_date()

#Time Until Jan 1st
import datetime

def time_until_new_year():
    now = datetime.datetime.now()
    next_year = now.year + 1

    jan1 = datetime.datetime(next_year, 1, 1)
    time_left = jan1 - now

    print("Time left until January 1st:")
    print(time_left)

time_until_new_year()

#Install the faker module and use it to create a list of dictionaries, where each dictionary represents a user with fake data.
from faker import Faker

fake = Faker()

# Step 3: Empty list to store users
users = []

# Step 4: Function to add fake users
def generate_users(num):
    for _ in range(num):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)

# Step 5: Call the function
generate_users(5)

# Print users list
for u in users:
    print(u)