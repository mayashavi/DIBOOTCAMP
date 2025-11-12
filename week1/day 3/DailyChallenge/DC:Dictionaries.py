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

#Clean the data: Remove $ + then convert to int
clean_wallet = int(wallet.replace('$',''))

#Create an empty list called basket
basket = []

for item, price in items_purchase.items():
    cleaned_price = int(price.replace('$','').replace(',',''))
    if cleaned_price <= clean_wallet:
        basket.append(item)
        clean_wallet -= cleaned_price
    else:
        continue
    if basket:
        print(sorted(basket))
    else:
        print("nothing")


#Check if the item is affordable (check the price):
# - if it is, add to the basket and take the price from the wallet
# - if not, skip it
# if we can't buy anything: print "nothing"
# if we can buy something: print the basket in the alphabetical order