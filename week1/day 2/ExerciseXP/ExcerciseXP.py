#1 Write code that concatenates two lists together without using the + sign.
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)

#2 Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
for calamaris in range(1500, 2501):
    if calamaris % 5 == 0 and calamaris % 7 == 0:
        print(calamaris)

#3 Check the index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Enter your name: ")

if user_name in names:
    index = names.index(user_name)
    print(f"{user_name} is in the list at index {index}.")
else:
    print("Sorry, your name is not in the list.")

#4 Ask the user for 3 numbers and print the greatest number.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

greatest = max(num1, num2, num3)

print("The greatest number is:", greatest)

#5 Alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")

#6 Find Letters in Words
words = []

for i in range(7):
    word = input(f"Enter word #{i + 1}: ")
    words.append(word)

letter = input("Enter a single letter: ")

# Loop through the list and find the first occurrence of the letter
for word in words:
    if letter in word:
        index = word.index(letter)
        print(f"In the word '{word}', the letter '{letter}' appears first at index {index}.")
    else:
        print(f"The letter '{letter}' does not appear in the word '{word}'.")
