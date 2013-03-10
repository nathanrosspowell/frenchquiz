#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# words. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Verbs, irregular ones have the variations in a dict. 
verbs = {
    "have" : {
        "i" : "j'ai",
        "you" : "tu as",
        "he" : "il a",
        "she" : "elle a",
        "we" : "nous avons", 
        "you(p)" : "vous avez",
        "they(m)" : "ils ont",
        "they(f)" : "elles ont",
    },
    "be" : {
        "i" : "je suis",
        "you" : "tu es",
        "he" : "il est",
        "she" : "elle est",
        "we" : "nous sommes", 
        "you(p)" : "vous etes",
        "they(m)" : "ils sont",
        "they(f)" : "elles sont",
    },
    "go" : {
        "i" : "je vais",
        "you" : "tu vais",
        "he" : "il va",
        "she" : "elle va",
        "we" : "nous allons", 
        "you(p)" : "vous allez",
        "they(m)" : "ils vont",
        "they(f)" : "elle vont",
    },
    # Group 1
    "like" : "aimer",
    "work" : "travailler",
    "eat" : "manager",
    "draw" : "dessiner",
    "bring" : "apporter",
    "sing" : "chanter",
    "compose" : "composer",
    "create" : "creer",
    "scream" : "crier",
    "give" : "donner",
    "study" : "etudier",
    "freeze" : "geler",
    "scratch" : "frotter",
    "play" : "jouer",
    "pardon" : "pardonner",
    "speak" : "parler",
    "share" : "partager",
    "jump" : "sauter",
    "carry" : "transporter",
	# Group 2
    "hate" : "hair",
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Regular verb roles. 
verb1Role = {
    "i" : ( "Je", "e", ),
    "you" : ( "tu", "es", ),
    "he" : ( "il", "e", ),
    "she" : ( "elle", "e", ),
    "we" : ( "nous", "ons", ), 
    "you(p)" : ( "vous", "ez", ),
    "they(m)" : ( "ils", "est", ),
    "they(f)" : ( "elles", "est", ),
}
# Regular verb roles. 
verb2Role = {
    "i" : ( "Je", "is", ),
    "you" : ( "tu", "is", ),
    "he" : ( "il", "it", ),
    "she" : ( "elle", "it", ),
    "we" : ( "nous", "essons", ), 
    "you(p)" : ( "vous", "essez", ),
    "they(m)" : ( "ils", "essent", ),
    "they(f)" : ( "elles", "essent", ),
}
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