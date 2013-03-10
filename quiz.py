#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# words. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from random import shuffle, randrange
# Local imports.
import words as frenchWords
import verbs as frenchVerbs
import buildVerb
import numbers as frenchNumbers
import buildNumber
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Simpler input.
def input( output ):
    return raw_input( output ).strip()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Quiz a range.
def quizRange( quizFunction, numberRange, trys = 3, shuffleThem = True ):
    if shuffleThem:
        shuffle( numberRange )
    items = len( numberRange )
    print "%s items in test:" % ( items, )
    correct = 0
    totalAttempts = 0
    firstQ = True
    for i, number in enumerate( numberRange ):
        if not firstQ:
            print "--------------"
        firstQ = False;
        print "%s) " % ( i + 1, ),
        answer, attempts = quizFunction( number, trys )
        totalAttempts += attempts
        if answer:
            correct += 1
    print "Score: %d/%d, total attempts: %d" % ( correct, items, totalAttempts, )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Quiz a number.
def quizNumber( number, trys = 3 ):
    word = getWord( number )
    print "What number is '%s'" % ( word, )
    answer = False
    totalAttempts = 0
    while trys > 0 and answer is False:
        totalAttempts += 1
        answerWord = input( "Answer> " )
        try: 
            answerNumber = int( answerWord )
            if answerNumber == number:
                answer = True
                print "Well done!"
            else:
                trys -= 1
                print "Incorrect."
                if trys > 0:
                    print "Please try again."
        except:
            print "Please entre a number."
    print "'%s' is the number %d" % ( word, number, )
    return answer, totalAttempts
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Quiz a word.
def quizWord( number, trys = 3 ):
    def cleanWord( theWord ):
        return theWord.replace( '-', ' ' ).strip()
    word = buildNumber.getWord( number )
    print "What is the word for '%d'" % ( number, )
    answer = False
    totalAttempts = 0
    while trys > 0 and answer is False:
        totalAttempts += 1
        answerWord = cleanWord( input( "Answer> " ) )
        if answerWord == cleanWord( word ):
            answer = True
            print "Well done!"
        else:
            trys -= 1
            print "Incorrect."
            if trys > 0:
                print "Please try again."
    print "'%s' is the number %d" % ( word, number, )
    return answer, totalAttempts
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# A bunch of number quiz functions
def quizLowNumbers( quizFunction, trys = 3 ):
    quizRange( quizFunction, range( 20 ), trys )
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
