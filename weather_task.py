# Make a weather/clothing project
# Ask for user input and depending on the response advise on their attire.
# prompt user for input, Evaluate each input and print the appropriate responses
# Follow these rules:
# when sunny >> respond with 'take your shorts!'
# stormy >> respond with 'take rain coat'
# rainy >> respond with 'Take your umbrella'
# rainy and stormy >> 'stay home'
# anything else respond with 'sorry, i didn't quite catch that'
# Make it so you keep playing until we say: 'No more Magic'

print("Welcome to the weather helper, if you need to leave please type")
print("'No more magic'")

while True:
    weather = input("Let me help you, can you tell me the weather outside?    ")
    if weather == 'rainy':
        print('Take umbrella')
    elif weather == 'sunny':
        print('wear sunglasses')
    elif ('rainy' in weather) and ('stormy' in weather):
        print('stay at home')
    elif weather == 'stormy':
        print('Take a coat')
    elif weather.lower().strip() == 'no more magic':
        break
    else:
        print("Sorry I didn't catch that, please try again")