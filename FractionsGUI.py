from tkinter import Button,Tk,Label
import random
from sensor import getScannedFraction


firstHalfOfQuestionList =  ["1/2", "1/2", "1/4", "1/6", "1/8", "1/10", "1/3", "1/2", "1/4", "1/8", "2/10", "1/10", "1/10", "1/4", "1/5",  "2/8", "2/6", "1/6", "1/6", "1/8", "1/6", "1/2"]
secondHalfOfQuestionList = ["1/4", "1/2", "1/4", "1/6", "1/8", "1/10", "1/6", "2/4", "2/8", "2/8", "2/10", "3/10", "2/10", "1/8", "1/10", "2/8", "2/6", "3/6", "2/6", "3/8", "2/6", "1/3"]

answers =                  ["3/4", "2/2", "2/4", "2/6", "2/8", "2/10", "3/6", "4/4", "4/8", "3/8", "4/10", "4/10", "3/10", "3/8", "3/10", "4/8", "4/6", "4/6", "3/6", "4/8", "3/6", "5/6"]
reducedAnswers =           ["3/4", "1/1", "1/2", "1/3", "1/4", "1/5",  "1/2", "1/1", "1/2", "3/8", "2/5",  "2/5",  "3/10", "3/8", "3/10", "1/2", "2/3", "2/3", "1/2", "1/2", "1/2", "5/6"]

def changeQuestion():
    
    global firstHalfOfQuestion
    global secondHalfOfQuestion
    
    global correctAnswer
    global correctReducedAnswer
    
    global amountOfTimesScannedCorrectly
    amountOfTimesScannedCorrectly = 0
    
    index = random.randint(0, len(firstHalfOfQuestionList) - 1) # pick a random question
    firstHalfOfQuestion = firstHalfOfQuestionList[index]
    secondHalfOfQuestion = secondHalfOfQuestionList[index]
    
    correctAnswer = answers[index] # get the answers to the selected question
    correctReducedAnswer = reducedAnswers[index]
    
    question.configure(text = "What is " + firstHalfOfQuestion + " + " + secondHalfOfQuestion + "?")

def checkCommonDenominator():
    
    userDenominator = int( getScannedFraction()[2:] )
    print ("Denominator: " + str(userDenominator) )
    #userDenominator = 4
    
    global commonDenominator
    commonDenominator = int(correctAnswer[2:])
    
    if userDenominator == commonDenominator:
        denominatorButton.grid_forget()
        answerButton.grid(row = 1, column = 0)
        feedback.configure(text = "")
    
    else: feedback.configure(text = "Please try again.")

def checkAnswer():
    
    scannedFraction = getScannedFraction()
    #scannedFraction = "1/4"
    print("Answer: " + str(scannedFraction) )
    correctNumerator = int(correctAnswer[0])
    
    if scannedFraction[2:] == correctAnswer[2:] and amountOfTimesScannedCorrectly < correctNumerator: # if the denominator is correct
        
        feedback.configure(text = "You're on the right track!")
        
        amountOfTimesScannedCorrectly = amountOfTimesScannedCorrectly + 1
    
    else:
        feedback.configure(text = "Please try again.") # if the denominator is incorrect
        amountOfTimesScannedCorrectly = 0 # restart
    
    if scannedFraction[2:] == correctAnswer[2:] and amountOfTimesScannedCorrectly == correctNumerator: # if the correct fraction was scanned as many times as the answer's numerator
        
        amountOfTimesScannedCorrectly = 0
        
        feedback.configure(text = "Correct!")
        answerButton.grid_forget()
        
        if correctAnswer == correctReducedAnswer: 
            denominatorButton.grid(row = 1, column = 0)
            changeQuestion()
            
        else: reducedAnswerButton.grid(row = 1, column = 0)
    
def checkReducedAnswer():
    
    scannedFraction = getScannedFraction()
    #scannedFraction = "3/4"
    print("Reduced Answer: " + str(scannedFraction) )
    correctNumerator = int(correctReducedAnswer[0])
    
    if scannedFraction[2:] == correctReducedAnswer[2:] and amountOfTimesScannedCorrectly < correctNumerator: # if the denominator is correct
        
        feedback.configure(text = "You're on the right track!")
        
        amountOfTimesScannedCorrectly = amountOfTimesScannedCorrectly + 1
    
    else:
        feedback.configure(text = "Please try again.") # if the denominator is incorrect
        amountOfTimesScannedCorrectly = 0 # restart
    
    if scannedFraction[2:] == correctReducedAnswer[2:] and amountOfTimesScannedCorrectly == correctNumerator: # if the correct fraction was scanned as many times as the answer's numerator
        
        amountOfTimesScannedCorrectly = 0
        
        feedback.configure(text = "Correct!")
        reducedAnswerButton.grid_forget()
        denominatorButton.grid(row = 1, column = 0)
        changeQuestion()

window = Tk() # GUI window
window.title("Interactive Fractions")

question = Label(window, text = "") 
changeQuestion()
question.grid(row = 0, column = 0)


denominatorButton = Button(window, text = "Confirm Common Denominator", command = checkCommonDenominator)
denominatorButton.grid(row = 1, column = 0)
answerButton = Button(window, text = "Confirm Answer", command = checkAnswer, width = 20)
reducedAnswerButton = Button(window, text = "Confirm Reduced Answer", command = checkReducedAnswer, width = 20)
feedback = Label(window, text = "") 
feedback.grid(row = 2, column = 0)
window.mainloop()

