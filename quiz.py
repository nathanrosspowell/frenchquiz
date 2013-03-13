#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# quiz. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from random import shuffle, randrange, sample
# Local imports.
import verbs as frenchVerbs
from buildQuiz import                   \
  makeFunctionItems                     \
, numberByNumber                        \
, numberByWord                          \
, quiz                                  \
, verbAndRole                           \
, verbRoleFrench                        \
, verbRoleEnglish
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# A bunch of number quiz'.
def quizLowNumbers( words = True, trys = 3 ):
    func = numberByWord if words else numberByNumber
    quiz( makeFunctionItems( func, range( 1, 21 ) ), trys )
def quizTensNumbers( words = True, trys = 3 ):
    func = numberByWord if words else numberByNumber
    quiz( makeFunctionItems( func, range( 10, 101, 10 ) ), trys )
def quizRandom( numbersList, take, words = True, trys = 3 ):
    func = numberByWord if words else numberByNumber
    numbers = sample( numbersList, take )
    quiz( makeFunctionItems( func, numbers, shuffleThem = False ), trys )
def quizBigNumbers( words = True, trys = 3 ):
    quizRandom( range( 101 ), 20, words = words, trys = trys )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# A bunch of number quiz'.
def quizIrregularVerbs( french = True, tests = 3, trys = 3 ):
    func = verbRoleFrench if french else verbRoleEnglish
    verbAndRole( verbRoleFrench, frenchVerbs.verbsIrregular, tests, trys )
def quizGroup1Verbs( french = True, tests = 3, trys = 3 ):
    func = verbRoleFrench if french else verbRoleEnglish
    verbAndRole( verbRoleFrench, frenchVerbs.verbsGroup1, tests, trys )
def quizGroup2Verbs( french = True, tests = 3, trys = 3 ):
    func = verbRoleFrench if french else verbRoleEnglish
    verbAndRole( verbRoleFrench, frenchVerbs.verbsGroup2, tests, trys )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
    #quizRandom( [ 1, 2, 3, 4, 5, 6, 7, 8 ], 4 )
    quizGroup1Verbs()