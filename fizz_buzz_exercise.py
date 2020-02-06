counter = 0
fail_code = ('You moron!!! Oh well try again (Remember, type exit to quit)')
print('Welcome to Fizz Buzz!!')
print('Count up one from 0, typing fizz for multiples of three')
print('and buzz for multiples of five. Type exit to stop the game')

while True:
    user_number = input(f'The current number is {counter}, type the next number...    ')
    counter += 1
    if user_number.lower() == 'exit':
        break
    elif user_number.lower().replace(" ", "") == 'fizzbuzz' and counter % 15 == 0:
        pass
    elif user_number.lower() == 'fizz' and counter % 15 == 0:
        print(fail_code)
        counter = 0
    elif user_number.lower() == 'buzz' and counter % 15 == 0:
        print(fail_code)
        counter = 0
    elif user_number.lower() == 'fizz' and counter % 3 == 0:
        pass
    elif user_number.lower() == 'buzz' and counter % 5 == 0:
        pass
    elif user_number >= 'A':
        print(fail_code)
        counter = 0
    elif int(user_number) % 3 == 0 and counter % 3 == 0:
        print(fail_code)
        counter = 0
    elif int(user_number) % 5 == 0 and counter % 5 == 0:
        print(fail_code)
        counter = 0
    elif (user_number) == str(counter):
        pass
    else:
        print(fail_code)
        counter = 0