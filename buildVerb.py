#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# words. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from verbs import *
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Build a irregular sentence. 
def getIrregularVerb( role, verb, thing ):
    return "%s %s" % ( verbs[ verb.lower() ][ role.lower() ], thing )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Build a regular sentence.
def getRegularVerb( role, verb, thing ):
    verb = verbs[ verb ]
    baseWord = verb[ : -2 ]
    ending = verb[ -2 : ]
    if ending == "er":
        verbRole = verb1Role
    elif ending == "ir":
        verbRole = verb2Role
    else:
        raise Exception( "Bad verb '%s'. No case for it." % ( verb, ) )
    start, ending = verbRole[ role ]
    return "%s %s%s %s" % ( start, baseWord, ending, thing, )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
    print getRegularVerb( "she", "hate", "you" )
