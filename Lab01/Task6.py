# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 20:50:51 2023

@author: AowenC
"""

class myList(list):        
    def power(self, x):
        for i in range(len(self)):
            self[i] = self[i] ** x
            
B = myList()
for i in range(5):
	B.append(i)

print(B)
B.power(2)

print(B)
B.reverse()

print(B)