#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 00:31:43 2023

@author: frasier
"""
import random

#Task 1
word_list = ["apple", "banana", "cherry", "date", "fig"]
print(word_list)

#Task 2
word = random.choice(word_list)
print(word)

#Task 3
guess = input("Enter a letter: ")

#Task 4
if len(guess) == 1 & guess.isalpha():
    print("Good guess!")
else: print("Oops! That is not a valid input.")

