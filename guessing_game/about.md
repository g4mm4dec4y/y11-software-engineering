# About Guessing Game.
---

## So... what is this?
This is a simple guessing game. 
The program decides on a number between 1 and 1000, and your job is to guess the number in 10 guesses. 
The game prompts the user with clues on whether their guess is lower or higher.
The user has the option to restart the game at the end. 

---

## Development:

### The coding
This game was developed rather simply. 
A function handles the generation of a random number that the user has to guess.
Another function handles the operation of the actual game.
This is done so that the game can be regenerated with ease.
Evrything was logically set out, however there were a few logic errors that required fixing.

### The debugging
One issue was forgetting to import random to be able to use the random function. *This was swiftly resolved.*
Another issue was that the code would not do anything when the user would guess the correct answer.
The program would simply keep asking for more guesses until the counter argument passed the limit, and then state that the user lost.
This was due to a misplaced break statememnt.
The break statement was tinkered around with and after placing it within the else: statement rather than after it.
Game executed correctly after this and was finalised.

### Screenshots
![simplicity of execution](guess_game_exec.png)
![random number function](guess_game_rangen.png)
