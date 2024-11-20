import random
def generate_number(start=1, end=100):
    return random.randint(start, end)

def check_guess(guess, target):
    if guess < target:
        print("Try Higher number")
    elif guess > target:
        print("Try Lower Number")
    else:
        print("Correct")