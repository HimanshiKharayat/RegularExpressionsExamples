# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:15:23 2020

@author: Lenovo
"""
import re

food = "hat rat mat pat"
#replace rat with food
# use pattern objects substitute is additional method in pattern objects
regex = re.compile("[r]at")
food = regex.sub("food",food)
print(food)
