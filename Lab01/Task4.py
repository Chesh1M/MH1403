# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 20:19:59 2023

@author: AowenC
"""

def f(x):
    newlist = []
    
    for num in range(1,x):
        if num % 11 == 0 or num % 17 == 0:
            newlist.append(num)
    
    total = sum(newlist)
    
    return total
    

while True:
    try:
        n = int(input("Please select a number greater than 0: "))
        
        if n > 0:
            total = f(n)
            print(total)
        else:
            print("Please select an integer greater than 0")
    except:
        print("Please select an integer")

