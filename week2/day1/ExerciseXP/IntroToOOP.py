#OOP: object oriented programming
#Class: blueprint of objects
#Attributes: a characteristic of an object
#Methods: functions related to a certain class
#Object/Instance: an example/one instance of the example, structured as a dictionary


#HOW TO CREATE A CLASS OF OBJECTCS
#init to initialize

class Dog:
    def __init__(self, name, sex, color, breed, age, is_trained): #the constructor function /// create defaullt value
        self.name = name
        self.sex = sex
        self.color = color
        self.breed = breed
        self.age = age
        self.is_trained = is_trained # = DEFAULT VALUE

    def bark(self): #function > method
        print(f'{self.name} goes Woof Woof\n'*self.age)
    
    def run(self):
        if self.age > 5:
            print(f'{self.name} prefers to walk.')
        else:
            print(f'{self.name} is running.')

    def walk(self, person):
        print(f'{person} is walking {self.name}.')

    def rename(self, new_name):
        self.name = new_name
        return self #EVERY METHOD SHOULD RETURN SELF

#HOW TO CREATE AN OBJECT OF A SPECIFIC CLASS
dog1 = Dog('Max', 'male', 'brown', 'poodle toy', 6, True)
print(dog1)

#Accessing the attributes of a dog:
print(dog1.name)
print(dog1.age)
print(dog1.is_trained)
print(dog1.__dict__) #internal dictionary

dog1.cuddly = True
print(dog1.cuddly)

#CREATE A SECOND OBJECT OF CLASS DOG dog2 and you choose attributes
dog2 = Dog('Oli', 'female', 'white', 'havanese', 8, True)
print(dog2.name)
print(dog2.sex)
print(dog2.__dict__)

#CALL THE METHOD: to a call method we need to use the object
dog1.bark()
dog2.bark()

#CREATE A METHOD, CALLED run() THAT CHECKS DOG'S AGE & IF DOG IS >5 YOU PRINT "dog.name prefers to walk", 
#else print "dog.name is running", then, call method

dog1.run()
dog2.run()

dog2.walk('John')
dog2.rename('Nini')
print(dog2.name)
print(dog2.__dict__)

#CREATE A CLASS CALLED "BankAccount", with 3 attributes: account holder (name + last name), account number, balance (50.00)
import datetime
class BankAccount:
    def __init__(self, account_holder, account_number, balance = 50.00):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.transaction = []
    
    def view_balance(self):
        self.transaction.append(f'{datetime.datetime.now()} --- view_balance')
        report = f'''account holder: {self.account_holder}
                    account number: {self.account_number}
                    balance: {self.balance}'''
        print(report)
    
    def deposit(self, amount):
        self.transaction.append(f'{datetime.datetime.now()} --- deposit {amount}')
        if amount <= 0: #less or equal than 0
            print('Invalid amount.')
        else:
            self.balance += amount
        self.view_balance()
        return self.balance

    def withdrawl(self, amount):
        self.transaction.append(f'{datetime.datetime.now()} --- withdraw {amount}')
        if amount <= 0:
            print('Invalid amount.')
        elif self.balance < amount:
            print('You don\'t have enough money.')
        else:
            self.balance -= amount
        self.view_balance()
        return self.balance

#creating the first amount on BankAccount:

acc1 = BankAccount('Sylvia Plath', '12345')
print(acc1)
acc1.view_balance()
acc1.deposit(6)
acc1.withdrawl(5)



