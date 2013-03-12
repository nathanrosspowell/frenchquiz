#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# buildQuiz. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from random import shuffle, randrange
from functools import partial
# Local imports.
import words as frenchWords
import verbs as frenchVerbs
import buildVerb
import numbers as frenchNumbers
import buildNumber
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Formatting.
div = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Simpler input.
def input( output ):
    return raw_input( output ).strip() #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Quiz a range.
def quiz( functionItems, trys = 3 ):
    numberItems = len( functionItems )
    print "%s items in test:" % ( numberItems, )
    correct = 0
    totalAttempts = 0
    for i, functionItem in enumerate( functionItems ):
        print "%s\n%s) " % ( div, i + 1, ),
        answer, attempts = functionItem( trys = trys )
        totalAttempts += attempts
        if answer:
            correct += 1
    returnVals = ( correct, numberItems, totalAttempts, )
    print "%s\nScore: %d/%d, total attempts: %d" % ( ( div, ) + returnVals )
    return returnVals
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Quiz a range.
def makeFunctionItems( quizFunction, items, shuffleThem = True ):
    if shuffleThem:
        shuffle( items )
    return [ partial( quizFunction, x ) for x in items ]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Quiz a number.
def tryLoopForItem( quizFunction ):
    def decorator( *args, **kwargs ):
        trys = kwargs.get( "trys", 1 )
        totalAttempts = 0
        answered = False
        while trys > 0 and answered is not True:
            totalAttempts += 1
            result, answer = quizFunction( *args, **kwargs )
            if result:
                answered = True
                print "Well done!"
            else:
                trys -= 1
                print "Incorrect."
                if trys > 0:
                    print "Please try again."
                else:
                    print "The correct answer is: %s" % ( answer, )
        return answered, totalAttempts
    return decorator
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write french word number as a digit.
@tryLoopForItem
def numberByNumber( number, trys = 3 ):
    word = buildNumber.getWord( number )
    print "What number is '%s'" % ( word, )
    answerWord = input( "Answer> " )
    answerNumber = int( answerWord )
    try: 
        answerNumber = int( answerWord )
    except:
        answerNumber = False
    return answerNumber == number, word
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write a digit as a french word
@tryLoopForItem
def numberByWord( number, trys = 3 ):
    def cleanWord( theWord ):
        return theWord.replace( '-', ' ' ).strip()
    word = buildNumber.getWord( number )
    print "What is the word for '%d'" % ( number, )
    answerWord = cleanWord( input( "Answer> " ) )
    return answerWord == cleanWord( word ), word
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
    quiz( makeFunctionItems( numberByNumber, range( 11 ) ), 2 )
