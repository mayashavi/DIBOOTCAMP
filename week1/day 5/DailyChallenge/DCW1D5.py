#Write a Python program that takes a single string of words as input, where the words are separated by commas
#The program should output these words sorted in alphabetical order, with the sorted words also separated by commas.

words = input('Enter words separated by commas: ')
word_list = words.split(',')
word_list.sort()

sorted_words = ",".join(word_list) #sort

print(sorted_words)

#Write a function that takes a sentence as input and returns the longest word in the sentence. 
#If there are multiple longest words, return the first one encountered. 
#Characters like apostrophes, commas, and periods should be considered part of the word.

def longest_word(sentence):
    words = sentence.split()
    longest = [] #empty string

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word("Margaret's toy is a pretty doll."))

