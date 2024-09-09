from unit1lesson2 import *

# Exercise 1 
#Using number_list.sort() to automatically sort the list in ascending order
#number_list.sort() 
#print ("The smallest number is",number_list[0])

# Exercise 2
# Condition that once the number in the number list is greater than 500, to print it and stop the list.
#number_list.sort()
#for num in number_list:
#    if num > 500:
#        print("The smallest number greater than 500 is",num)
#        break

# Exercise 3
# # Filters even numbers using modulo operator
# even_numbers = [x for x in number_list if x % 2 == 0]

# # Finds the smallest even number
# if even_numbers:
#     smallest_even = min(even_numbers)
#     print(f"The smallest even number is {smallest_even}")

# Exercise 4
# Using the max() function to find the last word alphabetically
# last_word = max(word_list)

# print(f"The word that is last alphabetically is {last_word}")

# Exercise 5
# Finds the word with the maximum length
longest_word = max(word_list, key=len)

print(f"The longest word is {longest_word}")