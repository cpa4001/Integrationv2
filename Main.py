# Christian Apostoli
# This will  be a trivia quiz which has
# a main theme based on JOJO's Bizzare Adventures.
# The quiz will  eventually have different question sets, and
# be more complex.

numCorrect = 0
print("Hello User")
startingScore = 100 / 100
print(" All new players will  start out with a score of", (startingScore * 100))
print(" A players final score will be determined by number of questions correct divided by total questions")
numCorrect = 100
numQuestions = 100
scoreFinal = numCorrect / numQuestions
print("For example, a perfect score will result in a", (int(scoreFinal) * 100))

n = int(input("What question level would you like to start at?"))
# We are going to ask the user what level they would like to start at
# The next function is going to provide the questions and will determine
# if the player is right ow wrong for each question

score = 0


def questionlevel():
    if n == 0:
        answer = input("In what part did Johnathan Joestar die?")
        if answer == 1 or answer == 'part 1' or answer == 'Part 1':
            score + 1
            print("Correct")
        else:
            print("Sorry, Incorrect")
    elif n == 1:
        answer = input("Who was Joseph's German friend who helped him defeat the pillar men?")
        if (answer == 'Stronheim') or (answer == 'Victor Von Stronheim'):
            score + 1
            print("Correct")
        else:
            print("Sorry, Incorrect")
    elif n == 2:
        answer = input("What was the tarot card of the Ship stand in part 3?")
        if answer == 'Strength':
            score + 1
            print("Correct")
        else:
            print("Sorry, Incorrect")
    elif n == 3:
        answer = input("What does famous phrase does DIO say as he is about to fight Jotaro?")
        if answer == 'I am approaching':
            score + 1
            print("Correct")
        else:
            print("Sorry, Incorrect")
    elif n == 4:
        answer = input("What is the final opening to part 4 (Just say the first two words)?")
        if (answer == 'Breakdown') or (answer == 'Shining Justice'):
            score + 1
            print("Correct")
        else:
            print("Sorry, Incorrect")
    elif n == 5:
        answer = input("What is Giorno Giovana's famous line (in Japanese)?")
        if answer == 'Kono Giorno Giovana niwa yume ga aru':
            score + 1
            print("Correct")
        else:
            print("Sorry, Incorrect")


questionlevel()
print("Your Final Score is ", (score * 100))
