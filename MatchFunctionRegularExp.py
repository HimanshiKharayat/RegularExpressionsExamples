# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:25:55 2020

@author: Lenovo
"""

# import re module 
import re

line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    print ("matchObj.group(1) : ", matchObj.group(1))
    print ("matchObj.group(2) : ", matchObj.group(2))
else:
    print ("No match!!")
    
    
    
Substring ='string'
String ='''We are learning regex with geeksforgeeks  
         regex is very useful for string matching. 
          It is fast too.'''
  
# Use of re.search() Method 
print(re.search(Substring, String, re.IGNORECASE)) 
  
# Use of re.match() Method 
print(re.match(Substring, String, re.IGNORECASE))