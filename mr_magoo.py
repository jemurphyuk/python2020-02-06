
print("Welcome to Mr. Magoo the Sensei, if you are at peace and wish to leave")
print("please tell him: 'I am at peace'")

while True:
    user_response = input("I am the wise Mr. Magoo, ask me something...    ")
    if user_response.lower().replace(" ", "") == 'iamatpeace':
        print('Sometimes what heart know, head forget')
        break
   # elif
    elif "?" in user_response:
        print('Questions are wise but for now wax on and off')

    else:
        print("Don't lose focus, wax on and off")