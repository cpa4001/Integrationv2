#Christian Apostoli
# This will  be a trivia quiz which has
# a main theme based on JOJO's Bizzare Adventures.
# The quiz will  eventually have different question sets, and
# be more complex.

from graphics import *
#------------- POP UP Graphics----------------------
# text pop up for game (will go before game logic)
win = GraphWin("JOJO Trivia Game", 600, 600)
def main(message, x):
    win.setBackground(color_rgb(0,0,0))

    txt = Text(Point(250,300), (message, x))
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

def text_box(message):
    win.setBackground(color_rgb(0,0,0))

    txt = Text(Point(250,300), message)
    txt.setTextColor(color_rgb(0,255, 200))
    txt.setSize(15)
    txt.draw(win)

    img = Image(Point(250,180), "Jojo.png")
    img.draw(win)

    input_box = Entry(Point(250, 400), 15)
    input_box.draw(win)
    answer = input_box.getText() 

    win.getMouse()
#-------------------------------------------------
main("Hello User, Welcome to my JOJO Trivia Game!", "")
clear()
main("All new players will  start out with a score of", 0)
clear()
main("A players final score will be \ndetermined by number of questions \ncorrect divided by total questions", '')
clear()

numCorrect = 100
numQuestions = 100
scoreFinal = numCorrect / numQuestions
scoreFinal = scoreFinal * 100

main("For example, a perfect score will result in a", scoreFinal)
clear()
main("First we will begin with a question that \ndepends on your desired difficuly, then \nwe will move on to a set of five questions" , '')
clear()
text_box("What question level would \nyou like to start at for your first set?")
# We are going to ask the user what level they would like to start at
# The next function is going to provide the questions and will determine
# if the player is right ow wrong for each question

arr = []
clear()

def questionlevelone():
    if answer == 0:
        text_box("In what part did Johnathan Joestar die?") 
        if answer == '1' or answer == 'part 1' or answer == 'Part 1':
            main("Correct", '')
            arr.append(1)
        else:
            main("Sorry" , "Incorrect")
