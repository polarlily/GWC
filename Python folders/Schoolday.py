start = '''
Your alarm clock rings, but you barely have the strength to open your eyes. You
hear the bus grind to a halt near your stop, and wonder if you should just skip.
'''

print(start)
done = False
finished = False

Middle = "You barely make the bus, but now you'are on your way to school."

Middle2 = '''You slump back into your plan, giddy at dreams of the city. But
your dreams are crushed when your mom flips the bed, and scolds you. After some
speeches, your mom decides to take you to school herself.'''

Middle3 = '''Option not valid, choose one of the options listed.(Though, you
should just pick ‘go’ since you’re such an idiot, anyway'''

do = '''You whip out your phone and hide it behind the desk.You're halfway
through the quiz when your teacher taps you on your shoulder with a disappointed
look. As you and your teacher take the walk of shame to the principal's office,
you ask your teacher how she knew."Nobody stares at their crotch for that long."
she answers.'''

yas = '''You pick up your pen with unsteady hands, already anticipating failure.
You struggle and your quiz is stained with tears. Just as you finished your sad
excuse for a quiz, you hear a buzz calling for yourcheck-out. Your mind goes
back to the time your mom promised to check you out. You rejoice and sprint out
of the room, ignoring the teacher's calls to return the quiz.'''


while not done:
    print("Type 'go' to go to school or 'ditch' to skip.")
    user_input = input()
    if user_input == "go":
        print(Middle)
        done = True

    elif user_input == "ditch":
        print(Middle2)
        done = True
    else:
        print(Middle3)
        done = False


print('''You walk into your classroom, and hear the groans of disappointment and
look to see the words POP QUIZ printed on the white board as blantant as a neon
sign. You are rushed to your seat and are about to start the quiz, but you
haven't study at all.''')

while not finished:
    print("Type 'cheat' to cheat on quiz or 'fail' to do quiz.")
    user_input = input()
    if user_input == "cheat":
        print(do)
        finished = True

    elif user_input == "fail":
        print(yas)
        finished = True

    else:
        print("Not valid, choose one of the actual options.")
        done = False


 #print(+++)


 #These are the second class outcomes!!!

 #

# print(''')
