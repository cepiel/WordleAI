from collections import Counter, defaultdict
import random
from words import *
from colorama import init, Back, Fore
from termcolor import colored

init(autoreset=True)
log_enabled = False

def init_wordle_ai(num_vowels, logging):
    global wordle_len 
    global answer
    global num_guesses
    global words_guessed
    global blacklisted
    global log_enabled
    log_enabled = logging
    answer = ""
    num_guesses = 0
    words_guessed = []
    blacklisted = set()
    wordle_len = len(word_list)
    
    # Randomly pick a word from the wordle dictionary
    answer = word_list[random.randint(0,wordle_len-1)]
    if print_enabled(): print(f'The answer is: {answer}' )
    return play(num_vowels)
    
def print_enabled():
    if log_enabled: return True
    else: return False
    
def play(num_vowels):    
    # For the first guess, pick a random word with 3+ vowels
    first_guess = find_word_with_vowels(num_vowels)
    guess_colors = guess_word(first_guess) 
    print_guess(guess_colors, first_guess)

    return keep_guessing(guess_colors)
    
        
def keep_guessing(guess_colors):
    while True:
        next_word = pick_next_word(guess_colors)
        guess_colors = guess_word(next_word) 
        if all(color == "green" for color in guess_colors.values()):
            return num_guesses
        else: print_guess(guess_colors, next_word)
        
        
        
def print_guess(guess_colors, guess):
    if print_enabled():
        for idx, color in enumerate(guess_colors):
            if guess_colors[idx] == "black": 
                print(Back.WHITE + Fore.BLACK + f' {guess[idx]} ', end=" ")
            elif guess_colors[idx] == "green": 
                print(Back.GREEN + Fore.BLACK + f' {guess[idx]} ', end=" ")
            elif guess_colors[idx] == "yellow": 
                print(Back.YELLOW + Fore.BLACK + f' {guess[idx]} ', end=" ")
        print("\n")
            
def find_word_with_vowels(num_vowels):
    while True:
        random_word = word_list[random.randint(0,wordle_len-1)]
        count_vowels = 0
        for vowel in vowels:
            if(vowel in random_word):
                count_vowels+=1
        if count_vowels >= num_vowels: return random_word
    
def guess_word(guess):
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
    
    if print_enabled(): print(f'Guess #{num_guesses}: {guess}')

    if guess == answer:
        for idx, g in enumerate(guess):
            guess_colors[idx] = "green"
        if print_enabled(): print("Correct!")
        print_guess(guess_colors, guess)
        return guess_colors
    else: 
        if print_enabled(): print("Incorrect. Guess again.")
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
    
def pick_next_word(guess_colors):
    global words_guessed
    
    last_word_guessed = words_guessed[-1]
    
    while True:
        next_word = word_list[random.randint(0,wordle_len-1)]
        if next_word in words_guessed: continue
        if check_black(guess_colors, next_word, last_word_guessed):
            if check_yellow_and_green(guess_colors, next_word, last_word_guessed):
                return next_word
            
        

def check_black(guess_colors, word, last_word_guessed):
    for b in blacklisted:
        if b in word: return False
    for idx, i in enumerate(last_word_guessed): 
        if guess_colors[idx] == "yellow" and word[idx] == i:
            return False
    return True
        
def check_yellow_and_green(guess_colors, word, last_word_guessed):
    
    # Check if there are any green spots that don't match this word
    for idx, i in enumerate(word): 
        if guess_colors[idx] == "green" and last_word_guessed[idx] != i: 
            return False
    
    # Count yellow and green letter counts to ensure the new word has the same counts
    count_y_g = defaultdict(int)
    for idx, g in enumerate(guess_colors):
        if guess_colors[idx] == "yellow" or guess_colors[idx] == "green":
           count_y_g[last_word_guessed[idx]] += 1
        
    next_word_letters = Counter(word)
    for letter in count_y_g.keys():
        if next_word_letters[letter] < count_y_g[letter]: 
            return False
    return True


init_wordle_ai(3, True)

