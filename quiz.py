#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# quiz. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from random import shuffle, randrange, sample
# Local imports.
import scoreQuiz
import verbs as frenchVerbs
from words import words as frenchWords
from buildQuiz import                   \
  makeFunctionItems                     \
, numberByNumber                        \
, numberByWord                          \
, quiz                                  \
, verbAndRole                           \
, verbRoleFrench                        \
, verbRoleEnglish                       \
, sentece                               \
, sentenceEnglish                       \
, sentenceFrench
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# A bunch of number quiz'.
def quizLowNumbers( words = True, trys = 3 ):
    func = numberByWord if words else numberByNumber
    return quiz( makeFunctionItems( func, range( 1, 21 ) ), trys )
def quizTensNumbers( words = True, trys = 3 ):
    func = numberByWord if words else numberByNumber
    return quiz( makeFunctionItems( func, range( 10, 101, 10 ) ), trys )
def quizRandom( numbersList, take, words = True, trys = 3 ):
    func = numberByWord if words else numberByNumber
    numbers = sample( numbersList, take )
    return quiz( makeFunctionItems( func, numbers, shuffleThem = False ), trys)
def quizBigNumbers( words = True, trys = 3 ):
    return quizRandom( range( 101 ), 20, words = words, trys = trys )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# A bunch of number quiz'.
def quizVerbs( french = True, tests = 3, trys = 3 ):
    func = verbRoleFrench if french else verbRoleEnglish
    return verbAndRole( func, frenchVerbs.verbs, tests, trys )
def quizIrregularVerbs( french = True, tests = 3, trys = 3 ):
    func = verbRoleFrench if french else verbRoleEnglish
    return verbAndRole( func, frenchVerbs.verbsIrregular, tests, trys )
def quizGroup1Verbs( french = True, tests = 3, trys = 3 ):
    func = verbRoleFrench if french else verbRoleEnglish
    return verbAndRole( func, frenchVerbs.verbsGroup1, tests, trys )
def quizGroup2Verbs( french = True, tests = 3, trys = 3 ):
    func = verbRoleFrench if french else verbRoleEnglish
    return verbAndRole( func, frenchVerbs.verbsGroup2, tests, trys )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# A bunch of number quiz'.
def quizSentence( french = True, tests = 3, trys = 3 ):
    func = sentenceFrench if french else sentenceEnglish
    return sentece( func, frenchVerbs.verbs, frenchWords, tests, trys )
def quizIrregularSentence( french = True, tests = 3, trys = 3 ):
    func = sentenceFrench if french else sentenceEnglish
    return sentece( func, frenchVerbs.verbsIrregular, frenchWords, tests, trys)
def quizGroup1Verbs( french = True, tests = 3, trys = 3 ):
    func = sentenceFrench if french else sentenceEnglish
    return sentece( func, frenchVerbs.verbsGroup1, frenchWords, tests, trys )
def quizGroup2Verbs( french = True, tests = 3, trys = 3 ):
    func = sentenceFrench if french else sentenceEnglish
    return sentece( func, frenchVerbs.verbsGroup2, frenchWords, tests, trys )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Big fat quiz.
def quiz1():
    s = scoreQuiz.Scores()
    print "~~~~ Low numbers"
    s.add( quizLowNumbers() )
    print "~~~~ Tens of numbers"
    s.add( quizTensNumbers() )
    print "~~~~ 10 Verbs and roles"
    s.add( quizVerbs() )
    print "~~~~ 10 sentences"
    s.add( quizSentence() )
    print "~~~~ Big numbers"
    s.add( quizBigNumbers() )
    s.present()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Quiz 2.
def quiz2():
    s = scoreQuiz.Scores()
    print "~~~~ Words and stuff"
    s.add( quizSentence() )
    s.present()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
    try:
        #quiz1()
        quiz2()
    except ( KeyboardInterrupt, SystemExit ):
        print "\n\nQUITTER!.....\n"
