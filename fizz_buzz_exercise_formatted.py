
def multiple15(num):
    return num % 15 == 0

def multiple5(num):
    return num % 5 == 0

def multiple3(num):
    return num % 3 == 0

def word_fizz(fizz):
    return fizz.lower() == 'fizz'

def word_buzz(buzz):
    return buzz.lower() == 'buzz'

counter = 0
fail_code = ('You moron!!! Oh well try again (Remember, type exit to quit)')
print('Welcome to Fizz Buzz!!')
print('Count up one from 0, typing fizz for multiples of three')
print('and buzz for multiples of five. Type exit to stop the game')

def fail_setting():
    return [fail_code, 0]

while True:
    user_number = input(f'The current number is {counter}, type the next number...    ')
    counter += 1
    if user_number.lower() == 'exit':
        break
    elif user_number.lower().replace(" ", "") == 'fizzbuzz' and multiple15(counter):
        pass
    elif (word_fizz(user_number) or word_buzz(user_number)) and multiple15(counter):
        print(fail_code)
        counter = 0
    elif word_fizz(user_number) and multiple3(counter):
        pass
    elif word_buzz(user_number) and multiple5(counter):
        pass
    elif user_number >= 'A':
        print(fail_code)
        counter = 0
    elif multiple3(float(user_number)) and multiple3(counter):
        print(fail_code)
        counter = 0
    elif multiple5(float(user_number)) and multiple5(counter):
        print(fail_code)
        counter = 0
    elif user_number == str(counter):
        pass
    else:
        print(fail_code)
        counter = 0