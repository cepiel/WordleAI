import random
from words import *

answer = ""
num_guesses = 0

words_guessed = []

def init_wordle():  
    wordle_len = word_list.len()
    # Randomly pick a word from the wordle dictionary
    answer = word_list.get(random.randint(0,wordle_len))
    print("The answer is: " + answer)
    play()
    
def play():
    # We now have 6 guesses to find the word
    
    # For the first guess, pick a random word with 3+ vowels
    first_guess = find_word_with_vowels(3)
    
    guess_colors = guess_word(first_guess) 
    print(guess_colors)

    pick_next_word(guess_colors)
    
    
    
    
def find_word_with_vowels(num_vowels):
    random_word = word_list.get(random.randint(0,wordle_len))
    count_vowels = 0
    for vowel in vowels:
        if(vowel in random_word):
            count_vowels+=1
    if count_vowels >= num_vowels: return random_word
    find_word_with_vowels(num_vowels)
    
def guess_word(guess):
    global words_guessed
    global num_guesses 
    guess_colors = {
        1: "black",
        2: "black",
        3: "black",
        4: "black",
        5: "black",
    }
    num_guesses += 1
    words_guessed.append(guess)
    
    print("Guess #"+num_guesses + ": " + guess)
    if guess is answer:
        print("Correct!")
        quit()
    else: 
        print("Incorrect. Guess again.")
        for idx, g in guess:
            if guess[idx] == answer[idx]: 
                guess_colors[idx] = "green"
            elif g in answer:
                guess_colors[idx] = "yellow"
            else:
                guess_colors[idx] = "black"
        return guess_colors
    
def pick_next_word(guess_colors):
    global words_guessed
    
    # optimize to search alphabetically in the future
    for word in word_list:
        if word in words_guessed: continue
        