import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed:
        try:
            player_guess = int(input("Make a guess: "))
            attempts += 1

            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
                
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()