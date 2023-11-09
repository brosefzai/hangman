#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 06:00:59 2023

@author: frasier
"""
import random
#word = "apple"
#list_of_guesses = []

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = [" _ " for x in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
'''
The above section initialises all the instance-variables used in a given instance of the game.
    word is a randomly-selected word from a list of words
    word_guessed is a censored representation of the word. It is a list where each item is a "_"
    num_letters is the number of letters of the random word
    num_lives is the number of lives recorded at any given stage of a game, initialised to 5
    word_list is the list of words given to the game from which it will choose a random word for us to guess
    list_of_guesses is the record of characters given as input, and is used to remind the user 
    of a character already guessed
'''
        
    def ask_for_input(self):
        while True:
            guess = input("Enter a letter: ")
            if guess.isalpha() == False or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

'''
The above section asks the user to input a guess, and checks that this guess is a 
single character, from the alphabet. It then checks to see if this letter has already been guessed
before, and informs the user if that is the case. Finally, it keeps a record of the guesses, to be
able to check if a given guess has already been asked.
'''

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            #self.num_lives -= 1
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[(self.word.index(letter))] = guess
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            
        #self.num_lives -= 1
'''
The above section takes such a (length-and-alphabet-verified) guess, converts it to lower case,
and then checks if this guess is a letter in the chosen random word (which was chosen at 
initialisation). If the guessed character is a letter in the word, a positive message is displayed
for the user, and a censored representation of the hidden random word has the matching character
revealed. If the guess was not in the word, a life is lost, and a message is displayed telling the
user that their guess was unsuccessful, as well as displaying the number of lives left.
'''