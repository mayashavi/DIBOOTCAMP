#4 Pillars of OOP: ABSTRACTION: Encapsulation: Polymorphism, Multiple Inheritance:

#INHERITANCE: PASSING ATTRIBUTES OR BEHAVIOR FROM A "FAMILY" MEMBER TO ANOTHER

#GENERAL CONCEPT OF INHERITANCE:
class Parent():
    def speak(self):
        print('Parent is speaking.')

class Child(Parent): #INHERITANCE
    def speak(self):
        print('Child is speaking.')
    pass

class Granchild(Child):
    pass

parent1 = Parent()
child1 = Child()
grandchild1 = Granchild()

parent1.speak()
child1.speak()
grandchild1.speak()

#Inheriting attributes:

class Animal:
    def __init__(self, name, family, legs, trained, age):
        self.name = name
        self.family = family
        self.legs = legs
        self.trained = trained
        self.age = age

    def sleep(self):
        return f"{self.name} is sleeping - ANIMAL"


class Dog(Animal):
    def __init__(self, name, family, legs, trained, age):
        super().__init__(name, family, legs, trained, age)


dog1 = Dog("Clifford", "Red Dog", "BIG", True, 4)
print(dog1.sleep())

#CREATE A CAT CLASS THAT INHERITS FROM ANIMAL ALL THE ANIMAL ATTRIBUTES + FRIENDLY AND HOUSE_CAT
#THEN CREATE AN OBJECT OF CAT AND PRINT IF IT IS FRIENDLTY OR NOT

class Cat(Animal):
    def __init__(self, name, family, legs, trained, age, house_cat=True):
        super().__init__(name, family, legs, trained, age)
        self.house_cat = house_cat

    def is_friendly(self):
        if self.trained:
            print("It's friendly!")
        else:
            print("Not friendly!")


cat1 = Cat("Toby", "Garfield Family", 4, True, 1)
cat1.is_friendly()


#MULTIPLE INHERITANCE:

class Alien(Dog):
    def __init__(self, name, family, legs, trained, age, planet):
        super().__init__(name, family, legs, trained, age)
        self.planet = planet

alien1 = Alien("JAN3T", "Space Dogs", 6, False, 300, "Venus")
print(alien1.sleep())
print(alien1.__dict__)
