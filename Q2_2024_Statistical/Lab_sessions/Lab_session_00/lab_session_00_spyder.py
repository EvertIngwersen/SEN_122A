# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:24:44 2024

@author: evert
"""

import pandas as pd
from pathlib import Path


dividend = 7
divisor = 3

quotient = dividend / divisor
int_quotient = int(quotient)

remainder = dividend % divisor 

#defining a list

# Lists

# Defining a list
this_is_an_empty_list = list()
this_is_also_an_empty_list = []
this_is_a_list = [4, 5, 'this is text', True]
print(f'The original list is: {this_is_a_list}')

# Accessing to elements
result1 = this_is_a_list[1]
print(f'The value in index 1 of list "this_is_a_list" is: {result1}')

# Adding elements
this_is_a_list.append(76)
print(f'After appending 76 to "this_is_a_list" is: {this_is_a_list}')

# Modifiying an element
this_is_a_list[2] = 'hello'
print(f'After editing the third element (index == 2): {this_is_a_list}')

# Removing the first element of the list
this_is_a_list.pop(0)
print(f'After deleting the first element: {this_is_a_list}')

# Tuples

#test_commit

# Defining a tuple
this_is_an_empty_tuple = tuple()
this_is_a_tuple = (3, True, 'Hello')
print(f'This is a tuple: {this_is_a_tuple}')

# Accessing to elements
result2 = this_is_a_tuple[1]
print(f'The value in index 1 of tuple is: {result2}')

# Uncomment the following line to see the error. What is happening?
#this_is_a_tuple[1] = 5

# Dictionaries

# Defining a dictionary
this_is_an_empty_dict = {}
birds = {'pn': 'Penguins', 'eg': 'Eagle', 'sg': 'seagull'}
print(f"The original bird dictionary is: {birds}")

# Accessing to dict element
result3 = birds['eg']
print(f"The bird with key 'eg' in dict is: {result3}")

# Adding elements
birds.update({'dc': 'duck'})
print(f"The new bird dictionary after adding one element is: {birds}")

# Deleting elements
del birds['pn']
print(f"The new bird dictionary after deleting one element is: {birds}")

#Excersise 2

dictionary = {'element_1': [2,3,4,5,6],
              'element_2': [2,4,8,16,32]}

dictionary.update({'element_3': [3,9,27,144,356]})

del dictionary['element_1']

#excersise 3

number_list = [3,6,1,7,2,8]


def sum_list(number_list):
    sum = 0
    for i in range(number_list):
        sum += i
    return sum
        
def get_mean(number_list):
    mean = sum_list(number_list) / len(number_list)
    return mean


# NOTE: We will use pathlib just to control file paths between UNIX and Windows


# Folder which contains the data
data_folder = Path('data')

# Reading an external dataset in csv
df = pd.read_csv(data_folder/'train.csv')

# Showing a sample of the first 10 rows of the database
df.head(10)
# Showing a Serie with all dtypes conteined in the DataFrame
df.dtypes









