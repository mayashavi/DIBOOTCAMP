#Loops Operators

#syntax of a loop:
#for <variable> in <sequence>:
#   an indented block of code (will happen within each iteration--> loop)

#Range() - helps us create a sequence of numbers
for num in range (1, 11, 2): #range (start=0, stop, step=1)
    print(num)

#enumerate() - gives as a tuple with index and item
student_info = ['Harry', 'Potter', 15, 'Privet Drive, 4', 'Hedwig', 'Buckbeak']

#without loop
student_info[0] = student_info[0].lower()

#lets change the items that are string to lowercase (with loop)
for i, item in enumerate(student_info): #using enumerate we have access to both: index and item
    if type(item) == str: #here we check type of item
        student_info[i]=item.lower() #here we reassign to lowercase

print(student_info)

#not for loop related: just useful in general
# zip() - can be used with any type of sequence

names = ('Patrick', 'Pete', 'Joe', 'Andy') #tuple
instruments = ['vocals', 'bass', 'guitar', 'drums'] #list

#names_instruments = {'Patrick', 'vocals'} - zip()

names_instruments = dict(zip(names, instruments))
print(names_instruments)