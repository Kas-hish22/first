import random
def main():
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = input("Enter your guess (1-100): ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        attempts += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Correct! The number was {number}. You guessed it in {attempts} attempts.")
            break
if __name__ == "__main__":
    main()
