
user_string = input("Enter a string (must be exactly 10 characters long): ")

if len(user_string) < 10:
    print("String not long enough.")
elif len(user_string) > 10:
    print("String too long.")
else:
    print("Perfect string!")
    
    print("First character:", user_string[0])
    print("Last character:", user_string[-1])

    print("\nBuilding the string:")
    output = ''
    for letter in user_string:
        output += letter
        print(output)