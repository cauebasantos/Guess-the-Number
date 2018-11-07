import random

def pick_up_number():
    return int(random.uniform(1, 101))

def is_too_high(guess, number):
    if guess > number :
        return True
    return False

def is_too_low(guess, number):
    if guess < number:
        return True
    return False

def is_equal(guess, number):
    if guess == number:
        return True
    return False

def print_introduction():
    print('---- Guess the Number ----')
    print('The computer has choosen a number, you have to guess it')
    print('Make your guess and we will try to help you')
    print('Good luck!')
    print('--------------------------')
    print()


print_introduction()

print('The game has began!')
print()

number = pick_up_number()

while True: 

    try:
        guess = input('Guess the number:   ')
        guess = int(guess)
    except:
        print('Please, try to put a valid number')
        continue

    if is_equal(guess, number):
        print()
        print(f'---- YOU WON! The hidden number was {number} ----')
        print()
        break
    elif is_too_high(guess, number):
        print('    UGHH, TOO HIGH...')
    else:
        print('    UGHH, TOO LOW...')

print('The game has come to the end, thank you for playing it!')
