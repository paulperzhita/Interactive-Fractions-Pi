from tkinter import Tk,Frame,Grid, Label, Button
import random
from sensor import getScannedFraction


firstHalfOfQuestionList =  ["1/2", "1/2", "1/4", "1/6", "1/8", "1/10", "1/3", "1/2", "1/4", "1/8", "2/10", "1/10", "1/10", "1/4", "1/5",  "2/8", "2/6", "1/6", "1/6", "1/8", "1/6", "1/2"]
secondHalfOfQuestionList = ["1/4", "1/2", "1/4", "1/6", "1/8", "1/10", "1/6", "2/4", "2/8", "2/8", "2/10", "3/10", "2/10", "1/8", "1/10", "2/8", "2/6", "3/6", "2/6", "3/8", "2/6", "1/3"]

answers =                  ["3/4", "2/2", "2/4", "2/6", "2/8", "2/10", "3/6", "4/4", "4/8", "3/8", "4/10", "4/10", "3/10", "3/8", "3/10", "4/8", "4/6", "4/6", "3/6", "4/8", "3/6", "5/6"]
reducedAnswers =           ["3/4", "1/1", "1/2", "1/3", "1/4", "1/5",  "1/2", "1/1", "1/2", "3/8", "2/5",  "2/5",  "3/10", "3/8", "3/10", "1/2", "2/3", "2/3", "1/2", "1/2", "1/2", "5/6"]

reducers =                 [  1  ,   2  ,   2  ,   2  ,   2  ,   2  ,    3  ,   4  ,   4  ,   1  ,   2  ,    2  ,    1   ,   1  ,   1   ,   4  ,   2  ,   2  ,   3  ,   4  ,   3  ,   1  ]

global currentStage 
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

def checkCommonDenominator():
    
    userDenominator = int( getScannedFraction()[2:] ) # import from sensor file
    
    global commonDenominator
    commonDenominator = int(correctAnswer[2:])

    global currentStage
    
    if userDenominator == commonDenominator: # if the user's denominator is correct, go to the next step
        denominatorButton.place_forget()
        answerButton.place(x=400, y=220, anchor="center")
        
        feedback.configure(text = "")
        hint.configure(text = "")
        currentStage = "unreduced"
    
    else: feedback.configure(text = "Please try again.")

def checkAnswer():
    
    scannedFraction = getScannedFraction()
    correctNumerator = int(correctAnswer[0])

    global amountOfTimesScannedCorrectly
    global currentStage
    
    if scannedFraction[2:] == correctAnswer[2:] and amountOfTimesScannedCorrectly < correctNumerator: # if the scanned fraction is correct but the user isn't finished yet
        
        feedback.configure(text = "You're on the right track!")
        
        amountOfTimesScannedCorrectly = amountOfTimesScannedCorrectly + 1
    
    else:
        feedback.configure(text = "Please try again.") # if the denominator is incorrect
        
        amountOfTimesScannedCorrectly = 0 # restart
    
    if scannedFraction[2:] == correctAnswer[2:] and amountOfTimesScannedCorrectly == correctNumerator: # if the correct fraction was scanned as many times as the answer's numerator
        
        amountOfTimesScannedCorrectly = 0
        
        hint.configure(text = "")
        feedback.configure(text = "Correct!")
        
        answerButton.place_forget()
        
        if correctAnswer == correctReducedAnswer: # if the answer is already reduced, ask a completely new question
            denominatorButton.place(x=400, y=220, anchor="center")
            changeQuestion()
            
        else:
            reducedAnswerButton.place(x=400, y=220, anchor="center") # otherwise, ask for the reduced answer
            currentStage = "reduced"
    
def checkReducedAnswer():
    
    scannedFraction = getScannedFraction()
    correctNumerator = int(correctReducedAnswer[0])

    global amountOfTimesScannedCorrectly
    
    if scannedFraction[2:] == correctReducedAnswer[2:] and amountOfTimesScannedCorrectly < correctNumerator: # if the denominator is correct
        
        feedback.configure(text = "You're on the right track!")
        
        amountOfTimesScannedCorrectly = amountOfTimesScannedCorrectly + 1
    
    else:
        feedback.configure(text = "Please try again.") # if the denominator is incorrect
        
        amountOfTimesScannedCorrectly = 0 # restart
    
    if scannedFraction[2:] == correctReducedAnswer[2:] and amountOfTimesScannedCorrectly == correctNumerator: # if the correct fraction was scanned as many times as the answer's numerator
        
        amountOfTimesScannedCorrectly = 0
        
        feedback.configure(text = "Correct!")
        hint.configure(text = "")
        
        reducedAnswerButton.place_forget()
        denominatorButton.place(x=400, y=220, anchor="center")
        changeQuestion()

def createHint():
    
    global currentStage
    global firstHalfOfQuestion
    global secondHalfOfQuestion
    
    if currentStage == "denominator":
        if firstHalfOfQuestion[2:] == secondHalfOfQuestion[2:]:
            hint.configure(text = "The denominators are already the same.")
        else:
            denominatorsList = [ int( firstHalfOfQuestion[2:] ), int(secondHalfOfQuestion[2:] ) ]
            biggerDenominator = max(denominatorsList)
            smallerDenominator = min(denominatorsList)
            hint.configure(text = str(biggerDenominator) + " is a multiple of " + str(smallerDenominator) )

    if currentStage == "reduced":
        hint.configure(text = "The numerator and denominator can be divided by " + str(reducer) )


app = Tk()
app.title("Interactive Fractions") # * Name of the window 

# * Main frame on which everything is added 
f = Frame(app,width=800,height=500)
f.grid(row=1,column=0,sticky="NW")
f.grid_propagate(0)
f.update()

# * Title Label 
title = Label(f,text="Welcome To Interactive Fractions")
title.config(font=("Roboto Slab", 20))
title.place(x=400, y=50, anchor="center")

# * Question Label
question = Label(f,text="")
changeQuestion()
question.config(font=("Roboto Slab", 15))
question.place(x=400, y=100, anchor="center")

# * Submit Button
denominatorButton=Button(f,text="Confirm Common Denominator", command = checkCommonDenominator)
denominatorButton.config(font=("Roboto Slab", 20))
denominatorButton.place(x=400, y=220, anchor="center")
answerButton = Button(f, text = "Confirm Unsimplified Answer", command = checkAnswer)
reducedAnswerButton = Button(f, text = "Confirm Simplified Answer", command = checkReducedAnswer)

# * Feedback Label 
feedback = Label(f, text = "")
feedback.place(x=400,y=270)

# * Hint Button
hintButton = Button(f, text = "Hint", command = createHint)
hintButton.place(x=400,y=320)


# * Hint Label
hint = Label(f,text="")
hint.config(font=("Roboto Slab", 15))
hint.place(x=400, y=380, anchor="center")

app.mainloop() # * Starts the GUI