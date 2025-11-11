student_info1 = ['Harry', 'Potter', 15, 'Privet Drive, 4', 'Hedwig', 'Buckbeak']

student_info = {'first_name': 'Harry', #String
                'last_name': 'Potter', #String
                'age': 15,
                'address': 'Privet Drive, 4',
                'pets': ['Hedwig', 'Buckbeak'], #Set []
                'best_friends': ('Ron Weasley', 'Hermoine Granger'), #Tuple ()
                'is_parselmouth': True, #Boolean
                'houses': {'main': 'Gryffyndor', 'second': 'Slytherin'}}

#loop in a list = directly
#for item in student_info1:
   # print(item)

#options of loops in dictionaries:

#access only keys = keys ()
for key in student_info.keys():
    print(key)

#access only values = values ()
for value in student_info.values():
    print(type(value))

#access both: keys and values
for key, value in student_info.items():
    print(key, value)

# Change all string values to uppercase
for key, value in student_info.items(): #accessing both keys and values
    if type(value) == str: #checking it's a string
        student_info[key] = value.upper() #changing value to upper case
print(student_info)

