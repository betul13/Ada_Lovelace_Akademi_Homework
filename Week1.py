
#WEEK 1



#Exercise 1:
#Write a function that receives a list as parameter and return how many elements it has; if it doesn't have any element return an error.

#Solution 1:

def length_list(entered_list):
    if entered_list:
        return len(entered_list)
    else:
        raise Exception("There is no element in the list")

input_str = input("Please enter a list elements separated by spaces: ")

entered_list = input_str.split()

entered_list = list(entered_list)

length_list(entered_list)

#Exercise 2:
#Write a function that receives a string as parameter and return the number of each character in it.

from collections import Counter

def count_characters(entered_string):
    char_counts = Counter(entered_string)
    return char_counts

entered_string = input("Please enter a string: ")
number_of_each_character = count_characters(entered_string)
print("number of each character:", number_of_each_character)
