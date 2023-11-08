#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 05:23:18 2023

@author: frasier
"""

#Milestone 3, Task 1
while True:
    guess = input("Enter a letter: ")
    if len(guess) == 1 & guess.isalpha():
        print("Good guess!")
        break
    else: print("Invalid letter. Please, enter a single alphabetical character.")