#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# words. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Globals.
singular = "singular"
plural = "plural"
verbs = "verbs"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Some French words with gender. 
words = {
    "table" : { 
        singular: ( "table", "la" ), 
        plural : ( "tables", "les" ),
        verbs : ( 
            "have",
            "create",
            "draw",
        )
    },
    "chicken" : {
        singular : ( "poulet", "du" ),
        plural : ( "poulets", "les" ),
        verbs : (
            "hate",
            "like",
            "eat",
        )
    },
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
    for english, french in words.items():
        print english, ":", french[ singular ][ 1 ], french[ singular ][ 0 ] 
