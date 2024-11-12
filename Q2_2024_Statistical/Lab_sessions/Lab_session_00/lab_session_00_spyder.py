# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:24:44 2024

@author: evert
"""

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