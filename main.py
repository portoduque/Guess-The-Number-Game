import random

EASY_TURNS = 10
HARD_TURNS = 5

#Set a randomly number for the answer
def set_answer():
    """return a randomly number between 1 and 100"""
    return random.randint(1,100)

#Set the turns corresponding with the difficult level
def set_difficulty():
    """Ask the difficult level and return the number of turns corresponding"""
    if input("Choose a difficulty level. Type 'easy' or 'hard': ").lower() == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS

#Check the guess and answer
def check_answer(answer_f,guess_f, turns_f):
    """Check if the guess is correct or not , and return the number of turns minus 1"""
    if guess_f > answer_f:
        print("\nToo High")
        return turns_f - 1
    elif answer_f > guess_f:
        print("\nToo Low")
        return turns_f - 1
    else:
        print(f"\nYou got it! The answer was {answer_f}.")

#Set the answer value
answer = set_answer()

#Print the welcomes
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {answer}")

#Set the game begin
def game():
    turns = set_difficulty()
    
    #Set the while loop
    guess = 0
    while guess != answer:  
        print(f"\nYou have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(answer,guess, turns)

        #Check if the game is over or not
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess == answer: 
            return
        else:
            print("Guess again.")

game()