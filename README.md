## Mastermind: color-guessing game
Mastermind is a coding-breaking board game.
The “secret code” is a set of 4 colors chosen out of a possible 6 colors, where the player needs to guess which colors are in which positions in the 4-color secret code. 

## How to run Mastermind
1. Download the repository
2. In the terminal with the current directory set to `mastermind`, enter:
```zsh
python3 mastermind.py
```

## How to play Mastermind
At the start of the program, it selects the 4 color secret code along with the 10 attempts with the scoring pegs beside.
After the program finished loading, the player can choose from the 6 colors at the bottom of screen to begin guessing.

After each guess, the player learns how many colors in their guess are in the right position, and how many had a color that’s in the code but the color is in the wrong position. 
Scoring pegs of different colors were used to show them how many correct guesses and how many correct positions they had gotten with their guess. 
Red pegs meant a correct color but out of position, black pegs meant a correct color in the correct position. 
These scoring pegs after each guess can be placed in any order – the player never knows _which_ colors are correct and/or in the correct position. 

The score is the number of guesses it takes the player to guess the code. 
The player loses if they don’t guess the code in 10 tries. 
Lower scores/fewer guesses are better. 
Our scoring pegs will be red for cows and black for bulls.

## Questions?
IF you have any questions or issues that need to be brought up, don't hesitate to reach me out at kim.huijuhn@gmail.com :)

