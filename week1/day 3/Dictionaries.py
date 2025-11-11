#DICTIONARIES: Complex data structure

student_info1 = ['Harry', 'Potter', 15, 'Privet Drive, 4', 'Hedwig', 'Buckbeak']

student_info = {'first_name': 'Harry', #String
                'last_name': 'Potter', #String
                'age': 15,
                'address': 'Privet Drive, 4',
                'pets': ['Hedwig', 'Buckbeak'], #Set
                'best_friends': ('Ron Weasley', 'Hermoine Granger'), #Tuple ()
                'is_parselmouth': True, #Boolean
                'houses': {'main': 'Gryffyndor', 'second': 'Slytherin'}}

#accessing data
print(student_info['first_name'])
print(student_info['pets'][1])
print(student_info)
print(student_info['houses']['main'])

#how to use methods on dictionary values
student_info['pets'].append('Toby')
print(student_info['pets'])
print(student_info['first_name'].upper())

#changing values of a dictionary
student_info[0] = 'John'
student_info['first_name'] = 'John'

#EXCERCISE
print(student_info['age']) #age
(student_info['age']) += 10
print(student_info['age']) #age + 10
(student_info['address']) = 'Betzalel 8' #change address
print(student_info['address'])
student_info['pets'].append('Doby')
print(student_info['pets']) #new pet to list
(student_info['is_parselmouth']) = False



#brackets: (tuple, function),[index, lists], {sets, dictionaries}

#set vs dictionary
my_set = {'Israel', 'US', 'Brazil'}
my_dict = {'name': 'Maya'}
print(type(my_set))
print(type(my_dict))