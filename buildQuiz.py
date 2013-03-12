#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# buildQuiz. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from random import shuffle, randrange, choice
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
    return raw_input( output ).strip()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
    return answerNumber == number, number
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
# Write verb and role
@tryLoopForItem
def verbRoleFrench( verb, trys = 3 ):
    role = choice( frenchVerbs.verbRoles )
    french, english = buildVerb.getVerbAndRole( role, verb )
    print "What is the french for '%s'?" % ( english, )
    answerWord = input( "Answer> " )
    return answerWord == french, french
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write verb and role
@tryLoopForItem
def verbRoleEnglish( verb, trys = 3 ):
    role = choice( frenchVerbs.verbRoles )
    french, english = buildVerb.getVerbAndRole( role, verb )
    print "What is the english for '%s'?" % ( french, )
    answerWord = input( "Answer> " )
    return answerWord == english, english
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write verb and role
def verbAndRole( quizFunction, verbGroup, take, trys = 3 ):
    keys = verbGroup.keys() 
    # Append the list until we have more items that the number of test.
    keysList = keys
    while len( keysList ) < take:
        keysList += keys
    shuffle( keysList )
    randomKeys = [ x for i, x in enumerate( keysList ) if i < take ]
    quiz( makeFunctionItems( quizFunction, randomKeys ), trys )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
    verbAndRole( verbRoleFrench, frenchVerbs.verbsGroup1, 4 )
