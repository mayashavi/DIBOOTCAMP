#Use the provided Pets and Cat classes to create a Siamese breed, instantiate cat objects, and use the Pets class to manage them.

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    pass

cat1 = Siamese('Barbie', 18)
cat2 = Bengal('Skipper', 14)
cat3 = Chartreux('Stacy', 9)

all_cats = [cat1, cat2, cat3]

sarahs_pets = Pets(all_cats)
sarahs_pets.walk()

#Goal: Create a Dog class with methods for barking, running speed, and fighting.
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        print("{self.name} is barking!")
        return self

    def run_speed(self):
        return (self.weight / self.age) * 10
        print("I'm running {result}.")
    
    def fight(self, other_dog):
        power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if power > other_power:
            return f"{self.name} wins against {other_dog.name}!"
        elif power < other_power:
            return f"{other_dog.name} wins against {self.name}!"
        else:
            return "It's a tie!"

dog1 = Dog('Ariel', 5, 45)
dog2 = Dog('Jasmine', 2, 60)

print(dog1.fight(dog2))

