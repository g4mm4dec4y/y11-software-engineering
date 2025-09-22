max_guess = 0
min_guess = 1000

def target_number():
    random_number = random_number.randint(min_guess, max_guess)
    return random_number

def game_start():
    valid = True
    number_of_guesses =  0
    game_number = target_number()
    while number_of_guesses <= 10:
        win = True
        guess = input("Guess a number: ")
        if guess != game_number:
            if guess > game_number:
                print("Lower\n")
            elif guess < game_number:
                print("Higher\n")
            number_of_guesses = number_of_guesses + 1
        else:
            print("Correct! You win.")
            break
    else:
        print("You lose.")
    
    restart = input("Would you like to play again?(y/n) ")
    while valid == True:
        if restart == y:
            valid = False
            game_start()
        elif restart == n:
            valid = False
            exit()
        else:
            print("Not an option.")


print("Welcome to the guessing game.")
print("I will think of a number from 1 to 1000 inclusive, and you have to guess.")
print("You will be guided through hints of higher or lower.")
print("Press enter to start.")
begin_game = input()
if input:
    game_start()