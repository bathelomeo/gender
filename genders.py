# import pyttsx3
# friend = pyttsx3.init()
# speech = input ("Say Something:")
# friend.say(speech)
# friend.runAndWait()

import pyttsx3
friend = pyttsx3.init()
friend.say('Hello')
friend.runAndWait()
Checking = input('How are you')

if Checking == 'Good':
   print('Great')
if Checking == 'Bad':
    print('I am very Sorry')

Check = input('How have you been')

if Check == 'Good':
   print('Great')
if Check == 'Bad':
    print('I am very Sorry')

Gender = input('What Gender are you')

Name = input ('What is your name')


if Gender == 'Male':
    friend.say("Welcome Mr." + str(Name))
if Gender == "Female":
    friend.say("Welcome Mrs. " + str(Name))
friend.runAndWait()