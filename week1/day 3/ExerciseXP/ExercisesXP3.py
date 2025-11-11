#1 Converting lists into dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

keys_values = dict(zip(keys, values))
print(keys_values)

#2 Ticket cost based on age
family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"{name}'s ticket price: ${price}")
    total_cost += price

print(f"\nTotal cost for the family: ${total_cost}")

#3 Create and manipulate dictionary

brand = {'name': 'Zara',
         'creation_date': 1975,
         'creator_name': 'Amancio Ortega Gaona',
         'type_of_clothes': ['men', 'women', 'children', 'home'],
         'international_competitors': ['Gap,' 'H&M', 'Benetton'],
         'number_of_stores': 7000,
         'major_color': {
             'France': 'blue',
             'Spain': 'red',
             'US': ['pink', 'green']
         }}

brand['number_of_stores'] = 2

print(f"Zara's clients are {brand['type_of_clothes']}.")

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print(brand['international_competitors'][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())

print(brand)

#4 
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

usersA = {name: index for index, name in enumerate(users)} #name --> index
usersB = {index: name for index, name in enumerate (users)} #index --> name
usersC = {name: index for index, name in enumerate(sorted(users))} #alphabetical

print(usersA)
print(usersB)
print(usersC)
