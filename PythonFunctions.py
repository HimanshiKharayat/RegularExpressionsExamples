# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:43:03 2020

@author: Lenovo
"""


def firstFunction(str):
    "This is my first python function"
    print(str)
    return


firstFunction("I am calling the first function")

#Pass by reference
#All parameters (arguments) in the Python language are passed by reference. 
#It means if you change what a parameter refers to within a function, 
#the change also reflects back in the calling function

def changedFunc(mylist):
    "This changes a passed list into the function"
    mylist.append([1,2,3,4,5])
    print("\nAppended list is", mylist)
    return

mylist=[12,13,14,15]
changedFunc(mylist)
print("\nList outside the changedListFuntion", mylist)


#Example where argument is being passed by reference and 
#the reference is being overwritten inside the called function
def changeMe(mylist1):
    "Changing mylist1 within the function does not affect mylist1."
    mylist1=[1,2,3,4,5]
    print("\nAppended list is", mylist1)
    return

mylist1=[12,13,14,15]
changeMe(mylist1)
print("\nList outside the changeFuntion", mylist1)


#required Function