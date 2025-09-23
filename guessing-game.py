import random
max_guess = 0
min_guess = 1000

#Function that generates a random number between 1 and 1000 inclusive
#Returns that number
def target_number():
    random_number = random.randint(max_guess, min_guess)
    return random_number

#Main game function
def game_start():
    valid = True
#Counter to keep track of how many guesses have been made
    number_of_guesses = 0
#Assigns a random number
    game_number = target_number()
#While loop keeps track ensuring only 10 guesses can be made
    while number_of_guesses <= 10:
        guess = input("Guess a number: ")
        if int(guess) != game_number:
        #Statements give hints as to where the number sits; above below
            if int(guess) > game_number:
                print("Lower\n")
            elif int(guess) < game_number:
                print("Higher\n")
            number_of_guesses = number_of_guesses + 1
            #Counter gets added to for keeping track
        elif int(guess) == game_number:
        #If user wins, the while loop is broken to continue to regeneration
            print("Correct! You win.\n")
            break
        else:
            print("Not a number.")
     #Message if lose
    else:
        print("You lose.")
    
    #This segment asks the user if they want to restart
    restart = input("\nWould you like to play again?(y/n) ")
    while valid == True:
        if restart == "y":
            valid = False
        #In which case the game function is called again
            game_start()
        elif restart == "n":
            valid = False
            exit()
        else:
            print("Not an option.")
        #The valid variable is to ensure that incorrect input options are caught

#Print statements as instructions for the user
print("Welcome to the guessing game.\n")
print("I will think of a number from 1 to 1000 inclusive, and you have to guess.\n")
print("You will be guided through hints of higher or lower.\n")
print("Press enter to start.\n")
#Starts when the user is ready
begin_game = input()
if input:
    game_start()