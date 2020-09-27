# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:42:14 2020

@author: Lenovo
"""


str1="Hello World!"
str2="Strings are a data type in python programming"
print(str1)
print(str2)

#String Slicing
print(str1[1:10:2])
print(str2[2:30:3])


newStr=str1[:6]
#String repetition
print(newStr*3)

#String formatting
age=22
name="HK"
print("I am %s and my age %d ."%(name,age))

