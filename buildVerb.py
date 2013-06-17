#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# words. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from verbs import *
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Build a irregular verb and role. 
def getIrregularVerb( role, verb ):
    return verbs[ verb.lower() ][ role.lower() ]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Build a regular verb and role.
def getRegularVerb( role, verb ):
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
    return "%s %s%s" % ( start, baseWord, ending, )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Build a verb and role. 
def getVerbAndRole( role, verb ):
    try:
        french = getIrregularVerb( role, verb )
    except:
        french = getRegularVerb( role, verb )
    english = "%s %s" % ( role.lower(), verb.lower(), )
    return french.lower().strip(), english.lower().strip()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
    print getRegularVerb( "she", "hate" )
