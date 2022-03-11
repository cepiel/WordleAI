from colorama import init

from AI import init_wordle_ai

vowel_count = 2
max_vowel_count = 4
max_data_count = 10
logging = False

while vowel_count <= max_vowel_count:
    
    data_count = 0
    num_guesses_data = []
    while data_count < max_data_count:
        data_count+=1
        num_guesses = init_wordle_ai(vowel_count, logging)
        num_guesses_data.append(num_guesses)
        
    added_guesses = sum(num_guesses_data)
    average = added_guesses/max_data_count
    print(f'In {max_data_count} trials, using a first guess with {vowel_count} vowels, average # of guesses to find the answer was: {average}')
    vowel_count+=1