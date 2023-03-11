# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:43:23 2023

@author: AowenC
"""

while True:
    try:
        n = int(input("Please select a number greater than 0: "))
        
        if n > 0:
            for i in range(n):
                print(i+1, end=' ')
        else:
            print("Please select an integer greater than 0")
    except:
        print("Please select an integer")