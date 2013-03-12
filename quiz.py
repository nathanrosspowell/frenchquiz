#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# quiz. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from random import shuffle, randrange
# Local imports.
from buildQuiz import                   \
  makeFunctionItems                     \
, numberByNumber                        \
, numberByWord                          \
, quiz
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
    shuffle( numbersList )
    numbers = [ x for i, x in enumerate( numbersList ) if i < take ]
    quiz( makeFunctionItems( func, numbers, shuffleThem = False ), trys )
def quizBigNumbers( words = True, trys = 3 ):
    quizRandom( range( 101 ), 20, words = words, trys = trys )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
    quizLowNumbers()
