#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 05:23:18 2023

@author: frasier
"""
word = "apple"

#Task 3

def ask_for_input():
    while True:
        guess = input("Enter a letter: ")
        if len(guess) == 1 & guess.isalpha():
            print("Good guess!")
            break
        else: print("Invalid letter. Please, enter a single alphabetical character.")
    
    check_guess(guess)
    
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else: print(f"Sorry, {guess} is not in the word. Try again.")