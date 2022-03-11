# Wordle
This program has 3 components. The primary one is a Wordle AI, which plays Wordle against itself and intelligently guesses the answer.

The second is a means of data collection, which runs multiple trials Wordle AI with different strategies to benchmark the success rate. 

The third lets you play Wordle traditionally, in the command line. 

## Wordle AI
The AI picks a word from the dictionary, and then tries to intelligently solve it, using the colored positional clues as hints. For those unfamiliar, Wordle colors each of the 5 letters of your guess one of three colors. 

- `Black`: that letter is not found in the answer word 
- `Yellow`: that letter is in the answer, but it is not in the correct position
- `Green`: that is the correct letter,  in the correct spot

The algorithm takes the color hints of previous guesses into consideration when searching the dictionary for the next suitable guess. I can proudly say, my Wordle algorithm has an average rate of ~5.5 guesses to the solution, so most of the time, it succeeds! Occasionally it gets stuck on tricky words which have a lot of similar words to it, where only 1 character differs. Don't we all get stumped sometimes? I remember when he was a baby algorithm and got stuck in infinite loops! Oh, they grow up so fast. Test this program by running  `AI.py` and watch the AI solve Wordle! Results printed to the command line.

## Wordle Data Collection
The data collection algorithm conducts trials a programmable amount of times, invoking the WordleAI. It also uses a strategy of having a first guess with more vowels in it. The data collection runs with a programmable range of numbers of vowels in the first guess, to see if that strategy makes a difference in getting to the answer quicker. To test this, run `data_collection.py` 

## Play Wordle 
This mode allows you to play traditional Wordle in the command line! You will be asked to input your guesses, and you have 6 guesses to get to the right answer. You will receive colored positional clues for each guess. It will also validate your guesses to ensure they are actual 5 letter words in the dictionary. Play by running `play_wordle.py`. 

## Setup
You may need to run `pip install colorama` and `pip install termcolor` to download the colored text dependencies before you run the apps.