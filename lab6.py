import data
from typing import Optional
from data import Book

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    min_dex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[min_dex]:
            min_dex = idx

    return min_dex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
#INPUT: List of book class
#OUTPUT: List of book class in alphabetical order according to the title object
def selection_sort_books(books:list[Book]) -> list[Book]:
    for i in range(len(books) - 1):                     #For every item in range(len of list - 1). Range(4-1) 0-2 . -1 because the right value has nothing to compare to in the end
        alpha = i                                           #Tracker for the alphabetically sorted book
        for j in range(i + 1, len(books)):                  #For every item starting from the 'second item' and range(0+1,4) so 1-3:
            if books[j].title < books[alpha].title:             #If Book title is greater than another alphabetically:
                alpha = j

        if alpha != i:                                  #Swap only if smaller author is found
            temp = books[i]
            books[i] = books[alpha]
            books[alpha] = temp
    return books

# Part 2
#INPUT: A single string
#OUTPUT: A single string whose uppercase letters become lowercased and lowercase letters become uppercased
def swap_case(x:str) -> str:
    result = ""                             #Empty string
    for character in x:                     #For every letter in string:
        if character.isupper():                 #If letter is uppercase:
            result += character.lower()             #Add that letter as a lowercase to the empty string
        elif character.islower():               #Elif letter is lowercase:
            result +=character.upper()              #Add that letter as an uppercase to the empty string
        else:                                   #Else:
            result +=character                      #Add character
    return result

# Part 3
#INPUT: A single string, a letter replacing the old letter in the string, state the old letter to be replaced.
#OUTPUT: Replace a certain letter from a string with a different letter
def str_translate(string:str, new_char:str, old_char:str) -> str:
    result = ""                             #Empty string
    for char in string:                     #For each letter in the string:
        if char == old_char:                    #If the letter is the old character:
            result += new_char                      #add the new letter to the empty list
        else:                                   #Else:
            result += char                          #add the letter regardless
    return result

# Part 4
#INPUT: A single string
#OUTPUT: A dictionary object for every word that appears. Should be a String: Integer pair
def histogram(string:str) -> dict:
    my_dict = {}                        #Empty dictionary
    words = string.split()              #Split the string into a list of strings

    for i in words:                     #For every item in the list of string:
        if i in my_dict:                    #If the item is in the dictionary:
            my_dict[i] += 1                     #Add 1 to the integer value
        else:                               #Else:
            my_dict[i] = 1                      #Add the string and make 1 the starting integer value
    return my_dict



