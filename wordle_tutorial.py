
# import your word dictionary here from another file

# The game is started (this function is called) by the last line in this file 
# TODO: part 1
def init_wordle_ai():
    # during this project, you may want to initialize global variables here at the beginning
    # global vars can be accessed anywhere in this file.
    # to edit a global var in another function, declare `global your_var_name` on one line, then `your_var_name = "whatever"` on another line after
    
    # I'll give you one to start with. use this to keep track of how many guesses the computer has made. 
    global num_guesses
    num_guesses = 0 # start it at 0
    
    global answer # declare the answer as a global
    
    global MAX_GUESSES
    MAX_GUESSES = 10 # some variables contain info that we won't want to change, but we need as a reference. instead of hard coding this number in a few places,
    # we define it at the top and reuse the variable anytime we need this number. this type of variable is called a CONSTANT and is usually capitalized. constant means it can't be changed once initialized
    # another benefit is we can easily change the behavior of our program by changing the constant at the top, and we don't have to dig around in our
    # code for every time we wrote `10` and change it to something else. 
    # bonus points: pass in a parameter to assign to the constant
    
    
    # Randomly pick a word from the wordle dictionary, print it out, and assign it to `answer`
    
    # Now we go to the main playing portion
    return gameplay_loop()

    
# what's the gameplay cycle for Wordle? 
# 1. Guess a word
# 2. get assigned colors for each letter based on a comparison to the answer
# 3. keep guessing until you get it correct or run out of guesses

# To start with lets implement a "dumb" wordle solver. Have it guess random dictionary words. 
# If it somehow finds the answer, have it finish the game. 
# Make the game end after a certain amount of guesses (maybe 10) otherwise you'll be here all day guessing 13,000 words. 
# After each guess, return a list of colors for each position:
    # Black = this letter isn't in the answer
    # Yellow = this letter is in the answer but isn't in the right position 
    # Green = correct letter in correct spot 
# We won't be using the colors yet, but implement the functionality for it here

# TODO part 2
def gameplay_loop():  
    print("Start game!")  
    
    # The gameplay 'cycle' could also be called a LOOP! What loop type would be good here? We want it to keep going forever, 
    # until we break out of it in one of 2 scenarios: the guess is correct, or you run out of guesses.
    
    # declare loop
        # within the loop, pick a random dictionary word as the guess and call it `guess`
        # then uncomment this line 
        # guess_colors = guess_word(guess)
        
        # come back after you finish guess_word() function
        # uncomment the next line and go to the print_guess() function
        # print_guess(guess_colors, guess)
        
        # now with the guess_colors returned, check if they're all green. 
        # if so, break out of the loop, print something about the computer winning, and quit the program
        # otherwise, do nothing, and the loop will repeat
        
        # how would we break out of the loop if the max number of guesses are exceeded? 
        # in that case, we want to print a fail message that the computer didn't guess the answer within the allotted guesses, and quit the program.
        
        
# TODO part 3        
# In this function, we want to check the guess against the answer, and RETURN a list of associated colors (black, yellow or green)
def guess_word(guess):
    # Let grab some of our global variables here. to ACCESS global vars, you don't have to grab them like this, 
    # but if you want to edit them (hint), you do have to say "global var_name" again, if you're in a different function from where they were declared (which we are)
    global num_guesses
    
    # I'll give you another variable. this is a dictionary. dicts have key/value pairs 
    # example: my_dictionary = {"key1": "value1", "key2": "value2", ...} 
    # and can be accessed like:    my_dictionary["key2"] which would return "value2"
    # a dictionary in this format (number, string) will let us easily visualize the guess colors for each position. 
    # the keys are positions in the word (position 0 = 1st letter, 1 = 2nd letter, etc)
    # the values can be a string representing the color. "black", "yellow", or "green". right now they're initialized to empty strings
    guess_colors = {
        0: "",
        1: "",
        2: "",
        3: "",
        4: "",
    }
    
    
    # print the guess number, and the guess word here like 'guess #1: flute' 


    # now for some good stuff! compare the guess and the answer
    # if the guess is exactly the same as the answer
        # change all the values in guess_colors to green
        # return the guess_colors
    # otherwise,
        # cycle through the word and check guess letter 1 against answer letter 1, guess letter 2 against answer letter 2, etc...
        # assign the correct color to each position
    
    
# TODO part 4   
# we know we want to print the answer many times throughout the program, so lets make it a function so we only have to write the code for that in 1 place!
# print the colors for each letter in the last guess 
# bonus points: print them on the same line, like wordle
def print_guess(guess_colors):
    print("") # have to put something within the function or python will be mad
            



# Huzzah! If you did all that, you should have a basic 'dumb' wordle solver! Run it and test it out. Use debug mode if things aren't working quite right to help find the issues

# TODO part 5
# Now for the `smart` solver...
# Instead of picking the next word randomly from the dictionary, call this function which will intelligently pick the next word
    # Pass the colors in as a parameter. 
    # Pick a word from the dictionary and check against the colors and the last guess to see if it is a likely candidate for the next guess. this part can get tricky
    # How would we get the last guess? Go back and figure out a way to get that value here
def pick_next_word():
    print("") 


# TODO part 6 - some bonus improvements 

# bonus points: COLOR each letter that you print so it looks like real wordle output! (hint: may need to download and import something for this. google it)
# bonus points for yellow which you'll need down the road: 
    # reference this picture https://www.reddit.com/r/wordle/comments/ry49ne/illustration_of_what_happens_when_your_guess_has/
    # yellow assignment gets tricky with double letters... 
    # refactor (meaning: rewrite/improve) your yellow color assignment with this in mind 
    # I found out I needed to do this because occasionally it would get stuck in an endless loop and couldn't find the answer and this was the culprit
# bonus points: don't just compare "black" letters for the LAST word guessed, you can rule out "black" letters for all previous guesses too, 
    # to make your next guess even more accurate. find a way to do this...
# bonus points: run the program a thousand times and record the results, calculate the average number of guesses to solve it. 
    # (I don't mean click it and write down the results that many times :P  you can easily do it programmatically)
    # for this, consider taking out the max guesses or increasing it substantially (a million or something) so you can catch the next part 
    # if the program gets hung up a long time, hit pause in the debug runner and see where it is. unpause and repause after a few more seconds. if its still hung on the same guess, it might have encountered a bug in your logic and can't find the answer. find out why and improve your code.

# this starts the game!
init_wordle_ai()

