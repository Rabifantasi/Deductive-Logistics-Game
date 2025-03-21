import random

def generate_secret_number():
    return str(random.randint(100, 999))

def evaluate_guess(secret, guess):
    feedback = []
    for i in range(3):
        if guess[i] == secret[i]:
            feedback.append("👌")  
        elif guess[i] in secret:
            feedback.append("👍")  
        else:
            feedback.append("❌")  
    return " ".join(feedback)

def play_game():
    secret_number = generate_secret_number()
    attempts = 10
    print("Welcome to the Guessing Game!")
    
    while attempts > 0:
        guess = input("Guess a 3-digit number: ")
        if not guess.isdigit() or len(guess) != 3:
            print("Invalid input! Please enter a 3-digit number.")
            continue
        
        feedback = evaluate_guess(secret_number, guess)
        print(feedback)
        
        if guess == secret_number:
            print("🎉 You Got IT!")
            return
        
        attempts -= 1
        print(f"Attempts left: {attempts}\n")
    
    print(f"Game Over! The correct number was {secret_number}.")


if __name__ == "__main__":
    play_game()