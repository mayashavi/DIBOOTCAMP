#1 Letter Index Challenge
word = input("Enter a word: ")

dictionary = {}
for index, letter in enumerate(word): #gives you index and letter
    if letter in dictionary:     # If the letter is already a key, append the new index
        dictionary[letter].append(index)
    else:     # If not, create a new key with the index in a list
        dictionary[letter] = [index]

print(dictionary)

#2 
# Given data
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# Step 1: Clean the data
# Remove $ and , then convert to int
clean_items = {item: int(price.replace("$", "").replace(",", "")) 
               for item, price in items_purchase.items()}
wallet_amount = int(wallet.replace("$", "").replace(",", ""))

basket = []

for item, price in clean_items.items():
    if wallet_amount >= price:
        basket.append(item)
        wallet_amount -= price

if len(basket) == 0:
    print("Nothing")
else:
    print(sorted(basket))