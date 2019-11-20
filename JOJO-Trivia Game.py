# Christian Apostoli
# This will  be a trivia quiz which has
# a main theme based on JOJO's Bizzare Adventures.
# The game has 2 sets of questions, one that varies
# on the players desired difficulty and 

from graphics import *

# ------------- POP UP Graphics----------------------
# text pop up for game 

# Creates Initial window with logo and becomes the
# main backdrop of the game
win = GraphWin("JOJO Trivia Game", 600, 600)


def newscene(message):
    win.setBackground(color_rgb(0, 0, 0))

    txt = Text(Point(250, 350), message)
    txt.setTextColor(color_rgb(0, 255, 200))
    txt.setSize(15)
    txt.draw(win)

    img = Image(Point(250, 180), "Jojo.png")
    img.draw(win)

    win.getMouse()


# Clears the screen for the next scene
def clear():
    rect = Rectangle(Point(0, 0), Point(600, 600))
    rect.setOutline(color_rgb(0, 0, 0))
    rect.setFill(color_rgb(0, 0, 0))
    rect.draw(win)


# Function that creates textbox for the user to enter info
# Function was very difficult to incorporate with other
# code, so it was commented for possible future use

## def text_box(message):
##    win.setBackground(color_rgb(0,0,0))
##
##    txt = Text(Point(250,300), message)
##    txt.setTextColor(color_rgb(0,255, 200))
##    txt.setSize(15)
##    txt.draw(win)
##
##    img = Image(Point(250,180), "Jojo.png")
##    img.draw(win)
##
##    input_box = Entry(Point(250, 400), 15)
##    input_box.draw(win)
##    answer = input_box.getText()
##
##    while True:
##        txt.setText(input_box.getText())
##
##    win.getMouse()
# -------------------------------------------------

newscene("Hello user, welcome to my JOJO Trivia Game!\n\
Continue the game by clicking the black window.")
clear()

newscene("All new players will start out with a score of " + str(0) + ".")
clear()

newscene("A player's final score will be determined by\n\
    the number of questions correct divided by total questions.")
clear()

numCorrect = 100
numQuestions = 100
scoreFinal = numCorrect / numQuestions
scoreFinal = scoreFinal * 100

newscene("For example, a perfect score will result in a " + str(scoreFinal) + ".")
clear()

newscene("    First we will begin with a question that depends on your\n\
desired difficuly, then we will move on to a set of five\n\
          questions. Please remember to answer your questions ASAP.")
clear()

newscene("What question level would you like to start at for your \n \
first set? Please return to the Python shell to insert\n \
       your input and drag the shell window beside the game window")
clear()

#  The program asks the user what level they would like to start at for
# their first set of quetions.
input_is_bad = True
while input_is_bad:
    try:
        n = int(input("What question level would you like to start\nat for your first set? (0-5, whole number)"))
        while n > 5 or n < 0:
            print("Number is out of range")
            n = int(input("What question level would you like to start\n\at for your first set? (0-5, whole number)"))
            input_is_bad = False
    except ValueError:
        print("This is not a whole number")

# This array is created to see if the user answered the question correctly
# by inserting a value in the array and checking  if the value is present.
arr = []


# This is the first set
# The question will vary based on the user's desired difficulty
# The following conditional statement provides the questions and will determine
# if the player is right or wrong for each question. This function is placed
# in the middle of the program to show the structure of the game rather
# than the function being at the top. 
def questionlevelone():
    if n == 0:
        answer = input("In what part did Johnathan Joestar die?")
        if answer == '1' or answer == 'part 1' or answer == 'Part 1':
            newscene("Correct, You get 1 point for your first set! Click to Continue")
            clear()
            arr.append(1)
        else:
            newscene("Sorry " + "Incorrect. Click to Continue")
            clear()
    elif n == 1:
        answer = input("Who was Joseph's German friend\nwho helped him defeat the pillar men? ")
        if (answer == 'Stronheim') or (answer == 'Victor Von Stronheim'):
            newscene("Correct, Click to Continue")
            clear()
            arr.append(1)
        else:
            newscene("Sorry, Incorrect. Click to Continue")
            clear()
    elif n == 2:
        answer = input("What was the tarot card of the Ship stand in part 3? ")
        if answer == 'Strength':
            newscene("Correct. Click to Continue.")
            clear()
            arr.append(1)
        else:
            newscene("Sorry, Incorrect. Click to Continue.")
            clear()
    elif n == 3:
        answer = input("What famous phrase does DIO\nsay as he is about to fight Jotaro? ")
        if answer == 'oh, so you are approaching me':
            newscene("Correct. Click to Continue")
            clear()
            arr.append(1)
        else:
            newscene("Sorry, Incorrect. Click to Continue")
            clear()
    elif n == 4:
        answer = input("What is the final opening to part 4(Just say the first two words)? ")
        if (answer == 'Breakdown') or (answer == 'Shining Justice'):
            newscene("Correct. Click to Continue")
            clear()
            arr.append(1)
        else:
            newscene("Sorry, Incorrect. Click to Continue")
            clear()
    elif n == 5:
        answer = input("What is Giorno Giovana's famous line (in Japanese)?")
        if answer == 'Kono Giorno Giovana niwa yume ga aru':
            newscene("Correct. Click to Continue")
            clear()
            arr.append(1)
        else:
            newscene("Sorry, Incorrect. Click to Continue")
            clear()


questionlevelone()

score = (arr.count(1) * 100)
newscene("Your Score for your first set is " + str(score))
clear()

newscene("Now time for your second set! There \n\
will be five questions. Click to continue.")
clear()

newscene("Remember to click until the question appears\n\
on the shell and then put in your answer")
clear()

# The following two arrays contain the questions
# and answers for the next set of questions.
secondSet = ["What is the stand of Fugo in part 5? ",
             "What is D'arby the youger's stand in part 3?  ",
             "What is shigechi's stand in part 4? ",
             "What does Jotaro have a PhD in? ",
             "What was the name of the supposed alien from part 4? "]

secondSetAnswers = ["Purple Haze", "Atum", "Harvest", "Marine Biology", "Mikitaka"]

scorearr = []
if arr.count(1) == 1:
    scorearr.append(1)

isOn = True

while isOn:
    for i in range(len(secondSet)):
        newscene(secondSet[i] + "\nClick to Continue")
        clear()
        question = input(secondSet[i])
        if question == secondSetAnswers[i]:
            newscene("That's Correct. Click to Continue")
            clear()
            print("That's Correct")
            scorearr.append(1)
        else:
            print("That's not correct.")
            newscene("That's not correct. Click to Continue")
            clear()

    isOn = False

scoreFinall = (int(scorearr.count(1)) / 6.0) * 100
print("Your Final Score is: ", format(scoreFinall, '.2f'))
newscene("Your Final Score is: " + format(scoreFinall, '.2f'))
clear()
newscene("Thanks for playing!")
win.close()
