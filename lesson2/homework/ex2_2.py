# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:11:46 2023

@author: leszek
"""

x = 5
print("part 1:")
print(x == 5 and 3)   ## True and Anything gives anything, in that case anything is 3
print(x == 4 and 3)   ##False and anything returns False
print(3 and x == 5)   ##True and True gives True
print(3 and x ==4)    ##True and False gives False
print("")
print ("part 2:")

print(isinstance(True, int))  ##gives True becasue True is integer 1

print(isinstance(True, bool)) ##gives True because True is also boolean