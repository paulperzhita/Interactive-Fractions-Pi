from Tkinter import *
import random
#import sensor.py


firstHalfOfQuestionList = ["1/3"] # ["1/2", "1/4", "1/6", "1/8", "1/10", "1/12", "1/3", "1/2", "2/4", "2/3"]
secondHalfOfQuestionList = ["1/6"] # ["1/2", "1/4", "1/6", "1/8", "1/10", "1/12", "1/6", "2/4", "3/6", "2/6"]
answers = []

correctAnswer = "3/4"

global amountOfTimesScannedCorrectly
amountOfTimesScannedCorrectly = 0

def changeQuestion():
    
    global firstHalfOfQuestion
    global secondHalfOfQuestion
    #global correctAnswer
    
    index = random.randint(0, len(firstHalfOfQuestionList) - 1)
    firstHalfOfQuestion = firstHalfOfQuestionList[index]
    secondHalfOfQuestion = secondHalfOfQuestionList[index]
    
    question.configure(text = "What is " + firstHalfOfQuestion + " + " + secondHalfOfQuestion)

def determineCommonDenominator():
    
    global commonDenominator
    firstCommonDenominator = int(firstHalfOfQuestion[2:]) # get the denominators for both halves of the question
    secondCommonDenominator = int(secondHalfOfQuestion[2:])
    
    biggerDenominator = max(firstCommonDenominator, secondCommonDenominator) # get biggest and smallest denominators from the 2 halves of the question
    smallerDenominator = min(firstCommonDenominator, secondCommonDenominator)
    
    if biggerDenominator == smallerDenominator:
        commonDenominator = biggerDenominator
    
    elif biggerDenominator % smallerDenominator == 0:
        commonDenominator = biggerDenominator
    
    else: commonDenominator = biggerDenominator * smallerDenominator

def checkCommonDenominator():
    
    userDenominator = 4
    determineCommonDenominator()
    
    if userDenominator == commonDenominator:
        denominatorButton.grid_forget()
        answerButton.grid(row = 1, column = 0)
        feedback.configure(text = "")
    
    else: feedback.configure(text = "Please try again.")

def checkAnswer():
    
    userAnswer = "1/4"
    correctNumerator = int(correctAnswer[0])
    #print correctNumerator
    
    if userAnswer[2:] == correctAnswer[2:] and amountOfTimesScannedCorrectly < correctNumerator: # if the answer is correct
        
        feedback.configure(text = "You're on the right track!")
        
        global amountOfTimesScannedCorrectly #= amountOfTimesScannedCorrectly + 1
        amountOfTimesScannedCorrectly = amountOfTimesScannedCorrectly + 1
    
    else:
        feedback.configure(text = "Please try again.") # if the answer is incorrect
    
    if userAnswer[2:] == correctAnswer[2:] and amountOfTimesScannedCorrectly == correctNumerator:
        
        global amountOfTimesScannedCorrectly
        amountOfTimesScannedCorrectly = 0
        
        feedback.configure(text = "Correct!")
        answerButton.grid_forget()
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

feedback = Label(window, text = "")
feedback.grid(row = 2, column = 0)

window.mainloop()

