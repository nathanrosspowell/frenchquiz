#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# buildQuiz. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from random import shuffle, randrange, choice, sample
from functools import partial
from functools import wraps
# Local imports.
from words import          \
  words as frenchWords     \
, singular as wordsSingular\
, verbs as wordsVerbs
import verbs as frenchVerbs
import buildVerb
import numbers as frenchNumbers
import buildNumber
import buildSentence
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Formatting.
div = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
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
    print div
    print "Score: %d/%d, total attempts: %d" % returnVals
    print div
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
    @wraps( quizFunction )
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
def verbRoleFrench( params, trys = 3 ):
    verb, role = params
    french, english = buildVerb.getVerbAndRole( role, verb )
    print "What is the french for '%s'?" % ( english, )
    answerWord = input( "Answer> " )
    return answerWord == french, french
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write verb and role
@tryLoopForItem
def verbRoleEnglish( params, trys = 3 ):
    verb, role = params
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
    r = lambda: choice( frenchVerbs.verbRoles )
    randomKeys = [ ( x, r() ) for x in sample( keysList, take ) ]
    return quiz( makeFunctionItems( quizFunction, randomKeys ), trys )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write sentence
@tryLoopForItem
def sentenceFrench( params, trys = 3 ):
    verb, role, item = params
    french, english = buildSentence.getSentence( role, verb, item )
    print "What is the french for '%s'?" % ( english, )
    answerWord = input( "Answer> " )
    return answerWord == french, french
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write sentence
@tryLoopForItem
def sentenceEnglish( params, trys = 3 ):
    verb, role, item = params
    french, english = buildSentence.getSentence( role, verb, item )
    print "What is the english for '%s'?" % ( french, )
    answerWord = input( "Answer> " )
    return answerWord == english, english
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write verb and role
def sentece( quizFunction, verbGroup, wordGroup, take, trys = 3 ):
    keys = verbGroup.keys() 
    wordKeys = wordGroup.keys()
    # Append the list until we have more items that the number of test.
    itemList = wordKeys
    while len( itemList ) < take:
        itemList += wordKeys
    v = lambda i: choice( frenchWords[ i ][ wordsVerbs ] ) # verb
    r = lambda: choice( frenchVerbs.verbRoles ) # role
    randomKeys = [ ( v( i ), r(), i ) for i in sample( itemList, take ) ]
    for r in randomKeys:
        print r
    return quiz( makeFunctionItems( quizFunction, randomKeys ), trys )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
    sentece( sentenceEnglish, frenchVerbs.verbsGroup1, frenchWords, 2 )
