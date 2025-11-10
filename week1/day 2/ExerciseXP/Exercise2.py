#1
my_fav_numbers = {0, 1, 3, 5, 10, 15, 20, 50, 100, 500}
my_fav_numbers.add(150)
my_fav_numbers.add(1000)

print(my_fav_numbers)

my_fav_numbers.remove(1000)

friend_fav_numbers = {2, 4, 12, 22, 44, 144, 222}
print(friend_fav_numbers)
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#2
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
new_tuple = my_tuple + (6, 7)
print(new_tuple)

#3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")
print("Number of 'Apples' in the list:", apple_count)

basket.clear()

print("Final basket:", basket)

#4
#Float: is a number with a decimal point
#Integer: is a whole number
my_list = []
num = 1.5
while num <= 5:
    my_list.append(num)
    num += 0.5

print(my_list)

#5
print("All numbers from 1 to 20:")
for num in range(1, 21):
    print(num)

print("\nNumbers where the index is even:")
numbers = list(range(1, 21))

for index in range(len(numbers)):
    if index % 2 == 0:
        print(f"Index {index}: {numbers[index]}")

#6
while True:
    name = input("Please enter your name: ")

    if not name.isdigit() and len(name) >= 3:
        print("Thank you!")
        break
    else:
        print("Invalid name. Please try again.")

#7
fav_fruits = input("What are your favorite fruits? (Seperated by spaces): ")
fav_fruits_list = fav_fruits.split()

chosen_fruit = input("Enter the name of a fruit: ")

if chosen_fruit in fav_fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

#8
toppings = []

base_price = 10
topping_price = 2.5

while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")

    if topping.lower() == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza.")
        toppings.append(topping)

total_cost = base_price + (len(toppings) * topping_price)

print("\nYour pizza toppings:")
for t in toppings:
    print(f"- {t}")

print(f"\nTotal cost: ${total_cost:.2f}")

#9
ages = []

while True:
    age_input = input("Enter the age of a family member (or type 'done' to finish): ")

    if age_input.lower() == 'done':
        break
    elif not age_input.isdigit():
        print("Please enter a valid number.")
        continue
    else:
        ages.append(int(age_input))

total_cost = 0

for age in ages:
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    total_cost += price

print(f"\nTotal ticket cost for your family is: ${total_cost}")

