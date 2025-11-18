class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def add_member(self, person):
        self.members.append(person)

    def born(self, first_name, age):
        # Create new Person with the family last name
        new_person = Person(first_name, age, self.last_name)
        self.members.append(new_person)
        return new_person

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return  
        print(f"No family member named {first_name} was found.")

    def family_presentation(self):
        print(f"Family Name: {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, Age: {member.age}")
