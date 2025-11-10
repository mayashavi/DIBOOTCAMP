mylist = ["apple", "banana", "cherry", 12, 1.09, True]
print(mylist)
print(mylist[2])
print(mylist[-2])
print(mylist[-1])

(mylist[2]) = "Pineapple"

print(mylist)

newlist = ["banana", "cherry", "kiwi", [1,3,5]]
print(newlist)

inside_list = newlist[3]
print('inside_list')
print(inside_list)
print(newlist[3])
print(inside_list[1])

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(grid[0][0])

#Adding items at the end of my list

mylist.append('this is the new last item')
print(mylist)

mylist.remove("apple")
print(mylist)

duplicates = ['first', 'second', 'first', 'third']

duplicates.remove ('first')
print(duplicates)

#.pop to remove number at index rather than by value/category

third_item = duplicates.pop(2)
print(duplicates)
print(third_item)

first = [1,2,3,4]
second = [5,6,7,8]

first.extend(second)
print(first)
print(first*3)

print(first + second)

print('hello'+' '+'world')
print('hello'*3)

print(len(first))
print(sum(first))
print(max(first))
print(min(first))

#Tuples
#cannot change what is inside the tuple (tuples are stuck)
tup = (1,2,3,4,'happy birthday')
print(tup)

a, b, c, d, e = tup

print(a)
print(b)
print(c)
print(d)
print(e)

#Sets

s = set([1,2,3,4,5,6,])
s.add(10)
print(s)
s.add(2)
print(s)

#Loops

li = [12,15,24,345,4656,54343,1331]

#for item in li:
   # if item > 200:
    #  print('Big number is', item)
  #  else:
 #       print('Small number is', item)
#mysum = 0

#for item in li:
 #   mysum = mysum + item
#    print('Current sum:', mysum)

#print('Final sum:', mysum)

##i = 0

#runs = int(input('how many times should we do it?'))
#while i < runs:
    #print(i)
   # i = i + 1

j = 0
while j < len(li):
    j = j + 1

#SECRET PASSWORD
password = 'secret'

guess = input('What is password?')

while guess != password:
    print('Incorrect password, try again')
    guess = input('What is password?')

print('Correct Password')

# Continue

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# Break

li = [12,15,264,234,12,577,109]

for item in li:
    if item > 500:
        print('Big number found', item)
        break
    print(item)
    print('random things happening until I find what Im looking for')