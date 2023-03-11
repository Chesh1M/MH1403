# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:52:12 2023

@author: AowenC
"""

while True:
    try:
        n = int(input("Please select a number greater than 0: "))
        
        if n > 0:
            newlist = [3*x+7 for x in range(n)]
            
            print(newlist)
        else:
            print("Please select an integer greater than 0")
    except:
        print("Please select an integer")