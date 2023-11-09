#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 06:22:54 2023

@author: frasier
"""
import random
word_list = ["apple", "banana", "cherry", "date", "grapefruit", "clementine", "orange", "fig", "olive", "persimmon"]


class Hangman:
    
    '''
    This class is used to initialise an instance of a game of Hangman.
    
    Attributes:
        word: a randomly-selected word from a list of words
        word_guessed: a censored representation of the word. It is a list where each item is a "_"
        num_letters: the number of letters of the random word
        num_lives: the number of lives recorded at any given stage of a game, initialised to 5
        word_list: the list of words given to the game from which it will choose a random word for us to guess
        list_of_guesses: the record of characters given as input, and is used to remind the user 
        of a character already guessed
    '''
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = [" _ " for x in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []


    def play_game(self, word_list):
        '''
        This function governs whether the entire game starts, has been won, or has been lost. It makes use
        of a while True loop which is only broken when one of these conditions have been met. A player loses
        when they have exhausted all their lives, and wins when they have no more letters left to guess.
        '''
        while True:
            if self.num_lives == 0:
                print("You lost!")
                print(f"The word was {self.word}")
                print(f"You got {self.word_guessed}")
                break
            elif self.num_letters > 0:
                self.ask_for_input()
            else:
                print("Congratulations. You won the game!")
                print(f"The word was {self.word}")
                break
                

    def ask_for_input(self):
        '''
        This function asks the user to input a guess, and checks that this guess is a 
        single character, from the alphabet. It then checks to see if this letter has already been guessed
        before, and informs the user if that is the case. Finally, it keeps a record of the guesses, to be
        able to check if a given guess has already been asked.
        '''
        guess = input("Enter a letter: ")
        if guess.isalpha() == False or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)


    def check_guess(self, guess):
        '''
        This function takes such a (length-and-alphabet-verified) guess, converts it to lower case,
        and then checks if this guess is a letter in the chosen random word (which was chosen at 
        initialisation). If the guessed character is a letter in the word, a positive message is displayed
        for the user, and a censored representation of the hidden random word has the matching character
        revealed. If the guess was not in the word, a life is lost, and a message is displayed telling the
        user that their guess was unsuccessful, as well as displaying the number of lives left.
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[(self.word.index(letter))] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
