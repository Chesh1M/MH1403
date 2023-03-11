# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:56:24 2023

@author: AowenC
"""

while True:
    try:
        n = int(input("Please select a number greater than 0: "))
        
        if n > 0:            
            for x in range(n):
                if x == 0 or x == n-1:
                    print("*" * n)
                else:
                    print("*" + " "*(n-2) + "*")
            
        else:
            print("Please select an integer greater than 0")
    except:
        print("Please select an integer")