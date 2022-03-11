from collections import Counter, defaultdict
import random
from words import *
from colorama import init, Back, Fore
from termcolor import colored

init(autoreset=True)

def init_wordle():
    global wordle_len 
    global answer
    global num_guesses
    global words_guessed
    global blacklisted
    answer = ""
    num_guesses = 0
    words_guessed = []
    blacklisted = set()
    wordle_len = len(word_list)
    
    # Randomly pick a word from the wordle dictionary as the answer
    answer = word_list[random.randint(0,wordle_len-1)]
    
    print(Back.GREEN + Fore.BLACK + "Welcome to Wordle! You have 6 guesses to find the correct 5-letter word. Good luck!")
    return play()
    
    
def play():  
    while True:  
        if num_guesses == 6:
            print("You did not win in 6 attempts. You lose.")
            quit()
        guess = input(f'Input Guess #{num_guesses+1}: ')
        guess_colors = guess_word(guess) 
        if type(guess_colors) == bool:
            if guess_colors == False: continue
        if all(color == "green" for color in guess_colors.values()):
            quit()
        else: print_guess(guess_colors, guess)
    
def print_guess(guess_colors, guess):
    for idx, color in enumerate(guess_colors):
        if guess_colors[idx] == "black": 
            print(Back.WHITE + Fore.BLACK + f' {guess[idx]} ', end=" ")
        elif guess_colors[idx] == "green": 
            print(Back.GREEN + Fore.BLACK + f' {guess[idx]} ', end=" ")
        elif guess_colors[idx] == "yellow": 
            print(Back.YELLOW + Fore.BLACK + f' {guess[idx]} ', end=" ")
    print("\n")
      
def validate_word(guess):
    if guess not in word_list:
        print("Invalid word! Guess again\n")
        return False

def guess_word(guess):
    if validate_word(guess) == False:
        return False
    global words_guessed
    global num_guesses 
    global answer
    global blacklisted
    guess_colors = {
        0: "",
        1: "",
        2: "",
        3: "",
        4: "",
    }
    num_guesses += 1
    words_guessed.append(guess)

    if guess == answer:
        for idx, g in enumerate(guess):
            guess_colors[idx] = "green"
        print_guess(guess_colors, guess)
        print("Correct! You win!")
        return guess_colors
    else: 
        print("Incorrect. Guess again.")
        for idx, g in enumerate(guess):
            if guess[idx] == answer[idx]: 
                guess_colors[idx] = "green"
            elif g not in answer:
                guess_colors[idx] = "black"
                blacklisted.add(g)
                
        guess_letters = Counter(guess)
        answer_letters = Counter(answer)
        for idx, g in enumerate(guess):
            if guess_colors[idx] == "":
                if answer_letters[g] < guess_letters[g]: 
                    guess_colors[idx] = "black"
                else: guess_colors[idx] = "yellow"
        return guess_colors

init_wordle()

