# Python Guessing Games

secret_text = "a"
user_guess = ""
user_attempts = 0
max_attempts = 3
exceeded_limit = False

# Start game
while user_guess != secret_text and not exceeded_limit:
    if user_attempts < max_attempts:
        user_guess = input("Enter a guess : ")
        user_attempts += 1
    else:
        exceeded_limit = True

# User has guessed correctly or game limit was reached
if exceeded_limit:
    print(5 * "-", "Game over ", 5 * "-")
    print("Max attempts : ", max_attempts)
    print("Total attempts : ", user_attempts)
else:
    print(5 * "*", "Congrats", 5 * "*")
    print("Max attempts : ", max_attempts)
    print("Total attempts : ", user_attempts)
    print("Correct guess : ", user_guess)

