#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# words. Authored by Nathan Ross Powell.
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
# Simpler input.
def input( output ):
    return raw_input( output ).strip() #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Quiz a range.
def quiz( functionItems, numberRange, trys = 3 ):
    numberItems = len( functionItems )
    print "%s items in test:" % ( numberItems, )
    correct = 0
    totalAttempts = 0
    for i, functionItem in enumerate( functionItems ):
        print "--------------\n%s) " % ( i + 1, ),
        answer, attempts = functionItem( trys = trys )
        totalAttempts += attempts
        if answer:
            correct += 1
    print "Score: %d/%d, total attempts: %d" % ( correct, numberItems, totalAttempts, )
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
        answer = False
        while trys > 0 and answer is False:
            totalAttempts += 1
            result, input = quizFunction( *args, **kwargs )
            if result:
                answer = True
                print "Well done!"
            else:
                trys -= 1
                print "Incorrect."
                if trys > 0:
                    print "Please try again."
        return answer, totalAttempts
    return decorator
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Quiz a number.
@tryLoopForItem
def quizNumber( number, trys = 3 ):
    word = buildNumber.getWord( number )
    print "What number is '%s'" % ( word, )
    answerWord = input( "Answer> " )
    answerNumber = int( answerWord )
    try: 
        answerNumber = int( answerWord )
    except:
        answerNumber = False
    return answerNumber == number, answerNumber
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Quiz a word.
@tryLoopForItem
def quizWord( number, trys = 3 ):
    def cleanWord( theWord ):
        return theWord.replace( '-', ' ' ).strip()
    word = buildNumber.getWord( number )
    print "What is the word for '%d'" % ( number, )
    answerWord = cleanWord( input( "Answer> " ) )
    return answerWord == cleanWord( word ), answerWord
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# A bunch of number quiz functions
def quizLowNumbers( quizFunction, trys = 3 ):
    quiz( makeFunctionItems( quizFunction, range( 2 ) ), trys )
def quizTensNumbers( quizFunction, trys = 3 ):
    quizRange( quizFunction, range( 20 ), trys )
def quizRandom( quizFunction, maxNumber, total, trys = 3 ):
    nums = range( maxNumber + 1 )
    shuffle( nums )
    nums = [ x for i, x in enumerate( nums ) if i < total ]
    quizRange( quizFunction, nums, trys, shuffleThem = False )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test run.
def frenchNumbersTestRun():
    printNumbers( min = 890, max = 910 )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
    print buildVerb.getVerbAndRole( "she", "hate" )
    quizLowNumbers( quizWord )
