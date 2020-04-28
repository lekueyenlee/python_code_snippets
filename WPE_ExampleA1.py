'''  Coding Exercise from Weekly Python Exercise
Getting input from the user
"while" loops
Converting data from strings to integers
Working with lists
The built-in "sum" function
The built-in "len" function
'''

import sys

list_numbers = []

user_input = input("Enter a number : ")


def get_output(in_list): 
    print("Sum of integers: " + str(sum(in_list)))
    print("Average value: " + str(sum(in_list)/len(in_list)))
    print("Max value: " + str(max(in_list)))
    print("Min value: " + str(min(in_list)))


while (user_input != ''): 
    list_numbers.append(int(user_input))
    user_input = input("Enter a number : ")

get_output(list_numbers)


sys.exit()


