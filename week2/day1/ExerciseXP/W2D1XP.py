#Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def oldest(cat1, cat2, cat3):
        oldest = cat1
        if cat2.age > oldest.age:
            oldest = cat2
        if cat3.age > oldest.age:
            oldest = cat3
        print(f'The oldest cat is {oldest.name} at {oldest.age} years old.')
        return oldest

cat1 = Cat('Superman', 6)
cat2 = Cat('Wonderwoman', 2)
cat3 = Cat('Batman', 10)

Cat.oldest(cat1, cat2, cat3)

#Create a Dog class, instantiate objects, call methods, and compare dog sizes.
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height*2} cm high!')

    def size(self, other_dog):
        if self.height > other_dog.height:
            print(f'{self.name} is bigger.')
        elif other_dog.height > self.height:
            print(f'{other_dog.name} is bigger.')
        else:
            print("Both dogs are the same size.")

davids_dog = Dog('The Joker', 132)
sarahs_dog = Dog('Lex Luthor', 150)

print(f'{davids_dog.name} is {davids_dog.height} cm tall.')
print(f'{sarahs_dog.name} is {sarahs_dog.height} cm tall.')

davids_dog.bark()
davids_dog.jump()

sarahs_dog.bark()
sarahs_dog.jump()

print(davids_dog.size(sarahs_dog))

#Create a Song class to represent song lyrics and print them
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)   

hallelujah = Song(['Now I\'ve heard', 'there was a secret chord', 'That David played,', 'and it pleased the Lord'])
hallelujah.sing_me_a_song()

#Create a Zoo class to manage animals. 
#The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animals(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
             print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
         print(f"{animal_sold} not found in the zoo.")

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped = {}

        for animal in sorted_animals:
            first_letter = animal[0].upper()

            if first_letter not in grouped:
                grouped[first_letter] = []
            
            grouped[first_letter].append(animal)

        return grouped

    def get_groups(self):
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")

my_zoo = Zoo("Fried Calamari")

# Add animals
my_zoo.add_animals("Baboon")
my_zoo.add_animals("Koala")
my_zoo.add_animals("Narwhal")
my_zoo.add_animals("Dolphin")
my_zoo.add_animals("Fried Calamari")
my_zoo.add_animals("Fresh Calamari")
my_zoo.add_animals("Manatee")

# Print full animal list
print("Animals in the zoo:")
my_zoo.get_animals()

# Sell one animal
print("\nSelling Dolphin...")
my_zoo.sell_animal("Dolphin")
my_zoo.get_animals()

#Show sorted & grouped animals
print("\nGrouped animals:")
my_zoo.get_groups()
