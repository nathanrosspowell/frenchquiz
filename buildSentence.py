#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# buildSentence. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from words import *
import buildVerb
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Build a sentence. 
def getSentence( role, verb, item ):
    verbRole = buildVerb.getVerbAndRole( role, verb )
    itemDetails = words.get( item, None )
    if itemDetails is None:
        word, gender = "table", "le"
    else:
        word, gender = itemDetails[ singular ] 
    french = "%s %s %s" % ( verbRole[ 0 ], gender, word, )
    english = "%s %s" % ( verbRole[ 1 ], item, )
    return french, english
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
    print getSentence( "she", "eat", "chicken" )
