#Christian Apostoli
# This will  be a trivia quiz which has
# a main theme based on JOJO's Bizzare Adventures.
# The quiz will  eventually have different question sets, and
# be more complex.

from graphics import *
#------------- POP UP Graphics----------------------
# text pop up for game (will go before game logic)
win = GraphWin("JOJO Trivia Game", 600, 600)
def main(message):
    win.setBackground(color_rgb(0,0,0))

    txt = Text(Point(250,350), message)
    txt.setTextColor(color_rgb(0,255, 200))
    txt.setSize(15)
    txt.draw(win)

    img = Image(Point(250,180), "Jojo.png")
    img.draw(win)
                      
    win.getMouse()
    win.close

def clear():
        rect = Rectangle(Point(0,0), Point(500,500))
        rect.setOutline(color_rgb(0,0,0))
        rect.setFill(color_rgb(0,0,0))
        rect.draw(win)

##def text_box(message):
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
#-------------------------------------------------

main("Hello User, Welcome to my JOJO Trivia Game!")
clear()
main("All new players will  start out with a score of " + str(0))
clear()
main("A players final score will be \ndetermined by number of questions \ncorrect divided by total questions")
clear()

numCorrect = 100
numQuestions = 100
scoreFinal = numCorrect / numQuestions
scoreFinal = scoreFinal * 100

main("For example, a perfect score will result in a " + str(scoreFinal))
clear()
main("First we will begin with a question that \ndepends on your desired difficuly, then \nwe will move on to a set of five questions\n please remember to answer your questions\n as fast as possible")
clear()
main("What question level would \nyou like to start at for your first set? \n please return to the Python shell to \n insert your input")
clear()
n = int(input("What question level would you like to start at for your first set?"))
# We are going to ask the user what level they would like to start at
# The next function is going to provide the questions and will determine
# if the player is right ow wrong for each question

arr = []

def questionlevelone():
    if n == 0:
        answer = input("In what part did Johnathan Joestar die?")
        if answer == '1' or answer == 'part 1' or answer == 'Part 1':
            main("Correct, You get 1 point for your first set!")
            clear()
            arr.append(1)
        else:
            main("Sorry " + "Incorrect")
            clear()
    elif n == 1:
        answer = input("Who was Joseph's German friend who helped him defeat the pillar men? ")
        if (answer == 'Stronheim') or (answer == 'Victor Von Stronheim'):
            main("Correct")
            clear()
            arr.append(1)
        else:
            main("Sorry, Incorrect")
            clear()
    elif n == 2:
        answer = input("What was the tarot card of the Ship stand in part 3? ")
        if answer == 'Strength':
            main("Correct")
            clear()
            arr.append(1)
        else:
            main("Sorry, Incorrect")
            clear()
    elif n == 3:
        answer = input("What does famous phrase does DIO say as he is about to fight Jotaro? ")
        if answer == 'I am approaching':
            main("Correct")
            clear()
            arr.append(1)
        else:
            main("Sorry, Incorrect")
            clear()
    elif n == 4:
        answer = input("What is the final opening to part 4 (Just say the first two words)? ")
        if (answer == 'Breakdown') or (answer == 'Shining Justice'):
            main("Correct")
            clear()
            arr.append(1)
        else:
            main("Sorry, Incorrect")
            clear()
    elif n == 5:
        answer = input("What is Giorno Giovana's famous line (in Japanese)?")
        if answer == 'Kono Giorno Giovana niwa yume ga aru':
            main("Correct")
            clear()
            arr.append(1)
        else:
            main("Sorry, Incorrect")
            clear()

questionlevelone()
score = (arr.count(1) * 100)
main("Your Score for your first set is " + str(score))
clear()
main("Now time for your second set!\n There will be five questions. Click to continue.")
clear()

main("Remember to click until the question appears on the shell\n and then put in your answer")
secondSet = ["What is the stand of Fugo in part 5? ",
             "What is D'arby the youger's stand in part 3? ",
             "What is shigechi's stand in part 4? ",
             "What does Jotaro have a PhD in? ",
             "What was the name of the supposed alien from part 4? "]

secondSetAnswers = ["Purple Haze", "Atum", "Harvest", "Marine Biology", "Mikitaka"]

scorearr = []
if arr.count(1) == 1:
    scorearr.append(1)
    
for i in range(len(secondSet)):
    main(secondSet[i])
    clear()
    question = input(secondSet[i])
    if question == secondSetAnswers[i]:
        main("That's Correct")
        clear()
        print("That's Correct")
        scorearr.append(1)
    else:
        print("That's not correct")
        main("That's not correct")
scoreFinall = (int(scorearr.count(1))/ 6.0) * 100
print("Your Final Score is: ", format(scoreFinall, '.2f'))
main("Your Final Score is: " + format(scoreFinall, '.2f'))
clear()
main("Thanks for playing!")
#win.close()
