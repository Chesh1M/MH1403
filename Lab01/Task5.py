# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 20:26:13 2023

@author: AowenC
"""

class Triangle:
    def __init__(self, a, b, c): # a, b, c values will be passed into here when instantiating the class
        self.a = a
        self.b = b
        self.c = c
        
    def is_valid(self):
        aMoreThanBAndC = self.a >= self.b + self.c # if a >= b + c, set aMoreThanBAndC to True
        bMoreThanAAndC = self.b >= self.a + self.c # if b >= a + c, set bMoreThanAAndC to True
        cMoreThanAAndB = self.c >= self.a + self.b # if c >= a + b, set cMoreThanAAndB to True
        
        self.valid = not (aMoreThanBAndC or bMoreThanAAndC or cMoreThanAAndB)
        # if either aMoreThanBAndC or bMoreThanAAndC or cMoreThanAAndB is True (meaning one side is longer than the sum of the other 2, set valid = not True AKA False)
        
    def computePeri(self):
        self.peri = self.a + self.b + self.c # calculates perimeter of triangle
        
    def printTriangle(self):
        print("Length of Triangle")
        print(f"Side A: {self.a} \t Side B: {self.b} \t Side C: {self.c}")
        print(f"Perimeter of Triangle: {self.peri}")
        print(f"Validity: {self.valid}")
        print()
        
        
triA = Triangle(2.1, 3.4, 5.2)
triA.is_valid()
triA.computePeri()
triA.printTriangle()

triB = Triangle(2, 3, 5)
triB.is_valid()
triB.computePeri()
triB.printTriangle()
        
        
        
        
        
        