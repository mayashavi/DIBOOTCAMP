# Coffee Shop Menu Manager

# Initial data
menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

# Step 2a: Define the show_menu() function
def show_menu(menu_dict):
    if menu_dict:  # checks if the dictionary
        print("Current menu:")
        for drink, price in menu_dict.items():
            print(f"{drink} - {price}₪")
    else:
        print("The menu is empty.")
        pass

show_menu(menu)

#Add drink
def add_item(menu_dict):
    drink = input("Enter new drink name: ").lower()
    if drink in menu_dict:
        print("Item already exists!")
    else:
        price = float(input("Enter price: "))
        menu_dict[drink] = price
        print(f'"{drink}" added!')
    pass
add_item(menu)

def update_price(menu_dict): #update_price = function name /// menu_dict = parameter
    drink = input("Enter the drink you want to update: ").lower()
    if drink in menu_dict:
        new_price = float(input("Enter the new price: "))
        menu_dict[drink] = new_price #replaces the old price with the new one
        print("Price updated!")
    else:
        print("Item not found.")
    pass
update_price(menu)

def delete_item(menu_dict):
    drink = input("Enter the drink you want to remove: ").lower()
    if drink in menu_dict:
        del menu_dict[drink]
        print("Item deleted.")
    else:
        print("Item not found.")
    pass
delete_item(menu)