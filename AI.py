from collections import Counter, defaultdict
import random
from words import *
from colorama import init, Back, Fore
from termcolor import colored

answer = ""
num_guesses = 0
wordle_len = 0
words_guessed = []
blacklisted = set()

def init_wordle():
    global wordle_len 
    global answer
    init(autoreset=True)
    wordle_len = len(word_list)
    # Randomly pick a word from the wordle dictionary
    answer = word_list[random.randint(0,wordle_len-1)]
    print(f'The answer is: {answer}' )
    play()
    
def play():    
    # For the first guess, pick a random word with 3+ vowels
    first_guess = find_word_with_vowels(3)
    
    guess_colors = guess_word(first_guess) 
    print_guess(guess_colors)

    while True:
        next_word = pick_next_word(guess_colors)
        guess_colors = guess_word(next_word) 
        print_guess(guess_colors)
    
def print_guess(guess_colors):
    for idx, color in enumerate(guess_colors):
        if guess_colors[idx] == "black": 
            print(Back.WHITE + Fore.BLACK + 'BLACK', end=" ")
        elif guess_colors[idx] == "green": 
            print(Back.GREEN + Fore.BLACK + 'GREEN', end=" ")
        elif guess_colors[idx] == "yellow": 
            print(Back.YELLOW + Fore.BLACK + 'YELLOW', end=" ")
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
    
    print(f'Guess #{num_guesses}: {guess}')

    if guess is answer:
        for idx, g in enumerate(guess):
            guess_colors[idx] = "green"
        print("Correct!")
        print_guess(guess_colors)
        quit()
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
    
def pick_next_word(guess_colors):
    global words_guessed
    
    # TODO optimize to check all, not just last word guessed
    last_word_guessed = words_guessed[-1]
    
    # TODO optimize to search alphabetically
    # if has first letter, search alphabetically, else pick random first word.
    while True:
        next_word = word_list[random.randint(0,wordle_len-1)]
        # print(f'Possible guess: {next_word}')
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
        # if letter not in word: 
        #     return False
    return True


init_wordle()
play()