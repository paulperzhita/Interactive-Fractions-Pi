from tkinter import Tk,Frame,Grid, Label, Button
import random
from sensor import getScannedFraction # imports a function that will determine the user's answer based on color

# questions and answers are currently hardcoded
firstHalfOfQuestionList =  ["1/2", "1/2", "1/4", "1/6", "1/8", "1/10", "1/3", "1/2", "1/4", "1/8", "2/10", "1/10", "1/10", "1/4", "1/5",  "2/8", "2/6", "1/6", "1/6", "1/8", "1/6"]#, "1/2"]
secondHalfOfQuestionList = ["1/4", "1/2", "1/4", "1/6", "1/8", "1/10", "1/6", "2/4", "2/8", "2/8", "2/10", "3/10", "2/10", "1/8", "1/10", "2/8", "2/6", "3/6", "2/6", "3/8", "2/6"]#, "1/3"]

answers =                  ["3/4", "2/2", "2/4", "2/6", "2/8", "2/10", "3/6", "4/4", "4/8", "3/8", "4/10", "4/10", "3/10", "3/8", "3/10", "4/8", "4/6", "4/6", "3/6", "4/8", "3/6", "5/6"]
reducedAnswers =           ["3/4", "1/1", "1/2", "1/3", "1/4", "1/5",  "1/2", "1/1", "1/2", "3/8", "2/5",  "2/5",  "3/10", "3/8", "3/10", "1/2", "2/3", "2/3", "1/2", "1/2", "1/2", "5/6"]

# the number that the user needs to divide by to reduce the answer
reducers =                 [  1  ,   2  ,   2  ,   2  ,   2  ,   2  ,    3  ,   4  ,   4  ,   1  ,   2  ,    2  ,    1   ,   1  ,   1   ,   4  ,   2  ,   2  ,   3  ,   4  ,   3  ,   1  ]

global currentStage # the current state of the application (denominator, unreduced, reduced)
currentStage = "denominator"

def changeQuestion(): 
    
    global firstHalfOfQuestion
    global secondHalfOfQuestion
    
    global correctAnswer
    global correctReducedAnswer
    global reducer
    
    global amountOfTimesScannedCorrectly
    amountOfTimesScannedCorrectly = 0
    
    index = random.randint(0, len(firstHalfOfQuestionList) - 1) # pick a random question
    firstHalfOfQuestion = firstHalfOfQuestionList[index]
    secondHalfOfQuestion = secondHalfOfQuestionList[index]
    reducer = reducers[index]
    
    correctAnswer = answers[index] # get the answers to the selected question
    correctReducedAnswer = reducedAnswers[index]
    
    question.configure(text = "What is " + firstHalfOfQuestion + " + " + secondHalfOfQuestion + "?")
    instructions.configure(text = "Begin Scanning The Common Denominator.")

def checkCommonDenominator(): # first step is to determine the common denominator
    
    userDenominator = int( getScannedFraction()[2:] ) # imported from sensor file to get the user's answer
    
    global commonDenominator
    commonDenominator = int(correctAnswer[2:]) # get the correct common denominator

    global currentStage
    
    if userDenominator == commonDenominator: # if the user's denominator is correct, go to the next step
        denominatorButton.place_forget()
        answerButton.place(x=300, y=250, anchor="center")
        
        feedback.configure(text = "Correct!")
        hint.configure(text = "")
        previousAnswer.configure( text = "Common Denominator: " + str(commonDenominator) )
        answerInProgress.configure(text = "Answer In Progress: " + " /" + str(commonDenominator) )
        instructions.configure(text = "Begin Scanning The Unsimplified Answer.")
        
        currentStage = "unreduced"
    
    else: feedback.configure(text = "Please try again.")

def checkAnswer(): # second step is to check the user's answer in unreduced form
    
    scannedFraction = getScannedFraction()
    correctNumerator = int(correctAnswer[0])

    feedback.configure(text = "")

    global amountOfTimesScannedCorrectly
    global currentStage
    global commonDenominator
    
    if scannedFraction[2:] == correctAnswer[2:] and amountOfTimesScannedCorrectly < correctNumerator: # if the scanned fraction is correct but the user isn't finished yet
        
        feedback.configure(text = "You're on the right track!")
        amountOfTimesScannedCorrectly = amountOfTimesScannedCorrectly + 1
        answerInProgress.configure(text = "Answer In Progress: " + str(amountOfTimesScannedCorrectly) + "/" + str(commonDenominator) )
    
    else: # if the scanned fraction is incorrect
        
        feedback.configure(text = "Please try again.") 
        amountOfTimesScannedCorrectly = 0 # reset
        answerInProgress.configure(text = "Answer In Progress: " + " /" + str(commonDenominator) )
    
    if scannedFraction[2:] == correctAnswer[2:] and amountOfTimesScannedCorrectly == correctNumerator: # if the correct fraction was scanned as many times as the correct numerator
        
        amountOfTimesScannedCorrectly = 0
        
        hint.configure(text = "")
        feedback.configure(text = "Correct!")
        
        answerButton.place_forget()
        
        if correctAnswer == correctReducedAnswer: # if the answer is already reduced, ask a completely new question

            currentStage = "denominator"
            denominatorButton.place(x=300, y=250, anchor="center")
            previousAnswer.configure(text = "")
            answerInProgress.configure(text = "")
            changeQuestion()
            
        else:
            
            reducedAnswerButton.place(x=300, y=250, anchor="center") # otherwise, ask for the reduced answer
            previousAnswer.configure( text = "Unsimplified Answer: " + correctAnswer[0] + "/" + str(commonDenominator) )
            answerInProgress.configure(text = "Answer In Progress: " + " /" )
            instructions.configure(text = "Begin Scanning The Simplified Answer.")
            currentStage = "reduced"
    
def checkReducedAnswer(): # third and final step is to give the answer in reduced form
    
    scannedFraction = getScannedFraction()
    correctNumerator = int(correctReducedAnswer[0])

    global amountOfTimesScannedCorrectly
    global currentStage
    
    if scannedFraction[2:] == correctReducedAnswer[2:] and amountOfTimesScannedCorrectly < correctNumerator: # if the denominator is correct
        
        feedback.configure(text = "You're on the right track!")
        amountOfTimesScannedCorrectly = amountOfTimesScannedCorrectly + 1
        answerInProgress.configure(text = "Answer In Progress: " + str(amountOfTimesScannedCorrectly) +  "/" + correctReducedAnswer[2:])
    
    else: # if incorrect
        
        feedback.configure(text = "Please try again.")
        amountOfTimesScannedCorrectly = 0 # restart
        answerInProgress.configure(text = "Answer In Progress: " + " / ")
    
    if scannedFraction[2:] == correctReducedAnswer[2:] and amountOfTimesScannedCorrectly == correctNumerator: # if the correct fraction was scanned as many times as the correct numerator
        
        amountOfTimesScannedCorrectly = 0
        currentStage = "denominator"
        
        feedback.configure(text = "Correct!")
        answerInProgress.configure(text = "")
        hint.configure(text = "")
        
        reducedAnswerButton.place_forget()
        denominatorButton.place(x=300, y=250, anchor="center")
        previousAnswer.configure(text = "")
        changeQuestion() # ask new question

def createHint(): # Hint button. Note: there are currently no hints for the unreduced state.
    
    global currentStage
    global firstHalfOfQuestion
    global secondHalfOfQuestion
    
    if currentStage == "denominator":
        if firstHalfOfQuestion[2:] == secondHalfOfQuestion[2:]: # if the denominators of both halves of the question are equal
            hint.configure(text = "The denominators are already the same.")
        
        else: # if they aren't equal, say that the bigger one is a multiple of the smaller one
            denominatorsList = [ int( firstHalfOfQuestion[2:] ), int(secondHalfOfQuestion[2:] ) ]
            biggerDenominator = max(denominatorsList)
            smallerDenominator = min(denominatorsList)
            hint.configure(text = str(biggerDenominator) + " is a multiple of " + str(smallerDenominator) )

    if currentStage == "reduced":
        hint.configure(text = "The numerator and denominator can be divided by " + str(reducer) )

def confirm(): # confirm button is placed on the screen but currently doesn't do anything.

    print("Confirm button is working!")

def reset(): # reset button

    global amountOfTimesScannedCorrectly
    global currentStage
    global commonDenominator
    
    amountOfTimesScannedCorrectly = 0

    if currentStage == "unreduced":
        answerInProgress.configure(text = "Answer In Progress: " + "/" + str(commonDenominator) )

    if currentStage == "reduced":
        answerInProgress.configure(text = "Answer In Progress: " +  "/" + correctReducedAnswer[2:])


app = Tk()
app.title("Interactive Fractions") # * Name of the window 

# * Main frame on which everything is added 
f = Frame(app,width=800,height=500)
f.grid(row=1,column=0,sticky="NW")
f.grid_propagate(0)
f.update()

# Elements are placed using a coordinate system.

# * Title Label 
title = Label(f,text="Welcome To Interactive Fractions!")
title.config(font=("Roboto Slab", 20))
title.place(x=400, y=30, anchor="center")

# * Question Label
question = Label(f,text="")
question.config(font=("Roboto Slab", 17))
question.place(x=400, y=80, anchor="center")

# * Previous Answer Label, gives answer from the previous stage of the question.
previousAnswer = Label(f,text="")
previousAnswer.config(font=("Roboto Slab", 15))
previousAnswer.place(x=400, y=120, anchor="center")

# * Answer In Progress Label, so user can see their answer as it is changing.
answerInProgress = Label(f,text="")
answerInProgress.config(font=("Roboto Slab", 15))
answerInProgress.place(x=400, y=160, anchor="center")

# * Instructions Label
instructions = Label(f,text="Please Scan The Common Denominator.")
instructions.config(font=("Roboto Slab", 15))
instructions.place(x=400, y=200, anchor="center")

# * Scan Button, each state currently has its own button, despite the buttons looking the same.
denominatorButton=Button(f,text="Scan", command = checkCommonDenominator)
denominatorButton.config(font=("Roboto Slab", 30))
denominatorButton.place(x=300, y=250, anchor="center") #400
answerButton = Button(f, text = "Scan", command = checkAnswer)
answerButton.config(font=("Roboto Slab", 30))
reducedAnswerButton = Button(f, text = "Scan", command = checkReducedAnswer)
reducedAnswerButton.config(font=("Roboto Slab", 30))

# * Confirm Button, this button is intended to confirm the user's answer rather than the scan button. It is currently not functional.
confirmButton = Button(f,text="Confirm", command = confirm)
confirmButton.config(font=("Roboto Slab", 30))
confirmButton.place(x=500, y=250, anchor="center")

# * Feedback Label, tells user if they are correct or if they should try again.
feedback = Label(f, text = "")
feedback.config(font=("Roboto Slab", 15))
feedback.place(x=320, y=280)

# * Hint Button
hintButton = Button(f, text = "Hint", command = createHint, anchor="center")
hintButton.config(font=("Roboto Slab", 20))
hintButton.place(x=350, y=342, anchor="center")

# * Hint Label
hint = Label(f,text="")
hint.config(font=("Roboto Slab", 15))
hint.place(x=400, y=380, anchor="center")

# * Reset Button
resetButton = Button(f, text = "Reset", command = reset, anchor="center")
resetButton.config(font=("Roboto Slab", 20))
resetButton.place(x=450,y=342,anchor="center")

changeQuestion()
app.mainloop() # * Starts the GUI
