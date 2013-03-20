#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# words. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Verbs, irregular ones have the variations in a dict.
verbsIrregular = {
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
        "they(f)" : "elles vont",
    },
}
verbsGroup1 = {
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
}
verbsGroup2 = {
	# Group 2
    "act" : "agir",
    "coution" : "avertir",
    "choose" : "choisir",
    "destroy" : "demolir",
    "disobey" : "desobeir",
    "establish" : "etablir",
    "daze" : "etourdir",
    "finish" : "finir",
    "groan" : "gemir",
    "cure" : "guerir",
    "hate" : "hair",
    "feed" : "nourrir",
    "obey" : "obeir",
    "pail" : "palir",
    "polish" : "polir",
    "decay" : "pourrir",
    "shorten" : "raccurcir",
    "slow down" : "ralentir",
    "fill" : "remplir",
    "divide" : "repatir",
    "roast" : "rotir",
    "salir" : "soil",
    "undergo" : "subir",
    "arise" : "unite",
    "unite" : "unir",
    "age" : "vielillir",
    "vomit" : "vomir",
}
verbs = {}
verbs.update( verbsIrregular )
verbs.update( verbsGroup1 )
verbs.update( verbsGroup2 )
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
verbRoles = verb1Role.keys()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
    import buildVerb
    print buildVerb.getVerbAndRole( "she", "hate" )
