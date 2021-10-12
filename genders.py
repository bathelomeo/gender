# import pyttsx3
# friend = pyttsx3.init()
# speech = input ("Say Something:")
# friend.say(speech)
# friend.runAndWait()

import pyttsx3
friend = pyttsx3.init()
Hello= input('Hello ')
Checking = input('How are you')
Check = input('How have you been')
Name = input ('What is your name')
Gender = input('What Gender are you')

if Check == 'Good':
   print('Great')
if Check == 'Bad':
    print('I am very Sorry')

if Gender == 'Male':
    friend.say("How are you Mr." + str(Name))
if Gender == "Female":
    friend.say("How are you Mrs. " + str(Name))
friend.runAndWait()