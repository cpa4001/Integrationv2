#Christian Apostoli
# This will  be a trivia quiz which has
# a main theme based on JOJO's Bizzare Adventures.
# The quiz will  eventually have different question sets, and
# be more complex.
from graphics import *
#------------- POP UP Graphics----------------------
##win = GraphWin("JOJO Trivia Game", 500, 500)
###Draws the background, image and text in a pop up window
##def main():
##    win.setBackground(color_rgb(0,0,0))
##
##    txt = Text(Point(250,300), "Hello User, Welcome to my JOJO Trivia Game!")
##    txt.setTextColor(color_rgb(0,255, 200))
##    txt.setSize(10)
##    txt.draw(win)
##
##    img = Image(Point(250,200), "Jojo.png")
##    img.draw(win)
##                      
##    win.getMouse()
### clears the screen and is very effective for creating new scenes
##def clear():
##        rect = Rectangle(Point(0,0), Point(500,500))
##        rect.setOutline(color_rgb(0,0,0))
##        rect.setFill(color_rgb(0,0,0))
##        rect.draw(win)
#-----------------------------------------------------

#main()
#clear()

# Game Logic
numCorrect = 0
startingScore = 100 / 100
print("Hello User, Welcome to my JOJO Trivia Game!")
print("All new players will  start out with a score of", 0)
print("A players final score will be determined by number of questions correct divided by total questions")
numCorrect = 100
numQuestions = 100
scoreFinal = numCorrect / numQuestions
print("For example, a perfect score will result in a", 100)
print("First we will begin with a question of that depends on your desired difficuly, then we will move on to a set of five questions")

n = int(input("What question level would you like to start at for your first set?"))
# We are going to ask the user what level they would like to start at
# The next function is going to provide the questions and will determine
# if the player is right ow wrong for each question

arr = []

def questionlevelone():
    if n == 0:
        answer = input("In what part did Johnathan Joestar die? ")
        if answer == '1' or answer == 'part 1' or answer == 'Part 1':
            print("Correct")
            arr.append(1)
        else:
            print("Sorry, Incorrect")
    elif n == 1:
        answer = input("Who was Joseph's German friend who helped him defeat the pillar men? ")
        if (answer == 'Stronheim') or (answer == 'Victor Von Stronheim'):
            print("Correct")
            arr.append(1)
        else:
            print("Sorry, Incorrect")
    elif n == 2:
        answer = input("What was the tarot card of the Ship stand in part 3? ")
        if answer == 'Strength':
            print("Correct")
            arr.append(1)
        else:
            print("Sorry, Incorrect")
    elif n == 3:
        answer = input("What does famous phrase does DIO say as he is about to fight Jotaro? ")
        if answer == 'I am approaching':
            print("Correct")
            arr.append(1)
        else:
            print("Sorry, Incorrect")
    elif n == 4:
        answer = input("What is the final opening to part 4 (Just say the first two words)? ")
        if (answer == 'Breakdown') or (answer == 'Shining Justice'):
            print("Correct")
            arr.append(1)
        else:
            print("Sorry, Incorrect")
    elif n == 5:
        answer = input("What is Giorno Giovana's famous line (in Japanese)?")
        if answer == 'Kono Giorno Giovana niwa yume ga aru':
            print("Correct")
            arr.append(1)
        else:
            print("Sorry, Incorrect")

questionlevelone()
score = (arr.count(1) * 100)
print("Your Score for your first set is ", score)


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
    question = input(secondSet[i])
    if question == secondSetAnswers[i]:
        print("That's Correct")
        scorearr.append(1)
    else:
        print("That's not correct")
scoreFinall = (int(scorearr.count(1))/ 6.0) * 100
print("Your Final Score is: ", format(scoreFinall, '.2f'))
#win.close()

