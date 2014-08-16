French Quiz
==========

Basic French language material with customizable quiz that has been written in Python.

Website
-------

There is also a website supporting this small set of scripts which can be found at [nathanrosspowell.github.io/frenchquiz](http://nathanrosspowell.github.io/frenchquiz).

It is developed on the [`gh-source`](https://github.com/nathanrosspowell/frenchquiz/tree/gh-source) branch and deployed to the [`gh-pages`](https://github.com/nathanrosspowell/frenchquiz/tree/gh-pages) branch.

Version
-------

These scripts use Python 2.7. It is tested on these OS's:

* Windows 7
* Ubuntu 12.04

#### Windows install

Python 2.7 is included in the standard Ubuntu 12.04 install. To get the needed software on windows, please download the [Python 2.7 MSI][winpy].

It is advised to put the Python install on your `Path` so you can simplify inovking of python scripts.
If not, try using the default Python path `C:\Python27\python.exe`

Running
-------

Go to the directory where you have the files and open a command line, type the following:

    python quiz.py
    
This will run the main quiz which is set up to do a big test on all topics.
If you want to do a specific test you can edit the part of the script under `if __name__ == "__main__":` or you can launch an interactive shell session.

#### Interactive shell session

Open a `cmd`. 
Use `pushd` to get to the folder with all the scripts in. 
Start a Python session with `python`.
Use `dir(quiz)` to list all the functions avaiable.
Pick one of the functions starting with 'quiz' e.g. `quizVerbs` and call it like `quiz.quizVerbs()`
Add the named parameter `tests` to increase the number of questions.

    C:\Users\npowell> pushd C:\Users\npowell\Downloads\frenchquiz-master
    C:\Users\npowell\Downloads\frenchquiz-master> python
    Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win
    32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import quiz
    >>> dir(quiz)
    ['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'frenchVerbs'
    , 'frenchWords', 'makeFunctionItems', 'numberByNumber', 'numberByWord', 'quiz',
    'quiz1', 'quizBigNumbers', 'quizGroup1Verbs', 'quizGroup2Verbs', 'quizIrregularS
    entence', 'quizIrregularVerbs', 'quizLowNumbers', 'quizRandom', 'quizSentence',
    'quizTensNumbers', 'quizVerbs', 'randrange', 'sample', 'scoreQuiz', 'sentece', '
    sentenceEnglish', 'sentenceFrench', 'shuffle', 'verbAndRole', 'verbRoleEnglish',
     'verbRoleFrench']
    >>> quiz.quizVerbs(tests=25)
    
Use `Ctrl+c` to exit out, or just close the `cmd` application.

[winpy]: http://www.python.org/ftp/python/2.7.3/python-2.7.3.msi "Python installer for Windows 7"

---
Revision Notes
==============

Section 1
--------

### The irregular verbs
These verbs have their own special conjugations, hence, irregular verbs.

    avoir   = to have
    être    = to be
    allez   = to go

### The conjugations

There are no set rules to these, just learn them.

#### Avoir

    i       = j'ai        - ( je + ai )
    you     = tu as       - ( "two ahh" )
    he      = il a
    she     = elle a
    we      = nous avons
    you(p)  = vous avez
    they(m) = ils ont
    they(f) = elles ont
    
#### Être

    i        = je suis
    you      = tu es 
    he       = il est
    she      = elle est
    we       = nous sommes 
    you(p)"  = vous etes
    they(m)" = ils sont
    they(f)" = elles sont

Some basic usage

    Je vais ai metro          = I go to the metro
    Tu vas a la bibliotheque  = We go to the library
    Vous allez a l'épicicerie = You go to the grocery store
    Il va au supermarket      = He goes to the supermarket

#### Allez

    i       = je vais
    you     = tu vais
    he      = il va
    she     = elle va
    we      = nous allons
    you(p)  = vous allez
    they(m) = ils vont
    they(f) = elles vont

Section 2
--------

### The numbers

The low numbers which are all used again for big numbers, e.g. 79 is read like 60-19

    0  = zero
    1  = un
    2  = deux
    3  = trois
    4  = quatre
    5  = cinq
    6  = six
    7  = sept
    8  = huit
    9  = neuf
    10 = dix
    11 = onze
    12 = douze
    13 = treize
    14 = quatorze
    15 = quinze
    16 = seize
    17 = dix-sept
    18 = dix-huit
    19 = dix-neuf
    20 = vingt
    
### The big numbers

Note again the way of making 70 and 90.

    10   = dix
    20   = vingt
    30   = trente
    40   = quarante
    50   = cinquante
    60   = soixante
    70   = soixante dix
    80   = quatre vingts
    90   = quatre vingts dix
    100  = cent
    1000 = mille
    
Section 3
--------

#### Family members

Father and son are masculine, the rest are feminine.

    the family = la familille
    mother     = la mere
    father     = le père
    son        = le fils       - ( "fiss" )
    daughter   = la fille      - ( "fee" )

Section 4
--------

### Group 1 verbs

These verbs ending in `er` all conjigate the same way.

    i       =    Je ****e
    you     =    tu ****es
    he      =    il ****e
    she     =  elle ****e
    we      =  nous ****ons
    you(p)  =  vous ****ez
    they(m) =   ils ****est
    they(f) = elles ****est
    
The verbs

    bring   = apporter
    carry   = transporter
    compose = composer
    create  = creer
    draw    = dessiner
    eat     = manager
    freeze  = geler
    give    = donner
    jump    = sauter
    like    = aimer
    pardon  = pardonner
    play    = jouer
    scratch = frotter
    scream  = crier
    share   = partager
    sing    = chanter
    speak   = parler
    study   = etudier
    work    = travailler
    
Some basic usage

    J'ai manger les pains                             = I eat bread
    Nous étudions le Français                         = We study French
    J'aime regarder les Simpsons chaque Vendredi soir = I like to watch The Simpson every Friday night
    
### Making a  negative sentence

You can add two words around the verb to make a sentence negative: `ne pas`

    Je parle Français              = I speak French
    Je ne parle pas Français       = I do not speak French
    Je n'aime pas manger les pains = I do not eat bread
    
Section 5
--------

### Group 1 verbs

These verbs ending in `ir` all conjigate the same way.

    i       =    Je *****is
    you     =    tu *****is
    he      =    il *****it
    she     =  elle *****it
    we      =  nous *****issons
    you(p)  =  vous *****issez
    they(m) =   ils *****issent
    they(f) = elles *****issent
    
The verbs

    act       = agir
    age       = vielillir
    arise     = unite
    choose    = choisir
    coution   = avertir
    cure      = guerir
    daze      = etourdir
    decay     = pourrir
    destroy   = demolir
    disobey   = desobeir
    divide    = repatir
    establish = etablir
    feed      = nourrir
    fill      = remplir
    finish    = finir
    groan     = gemir
    hate      = hair
    obey      = obeir
    pail      = palir
    polish    = polir
    roast     = rotir
    shorten   = raccurcir
    slow down = ralentir
    soil      = salir
    undergo   = subir
    unite     = unir
    vomit     = vomir
    
Section 6
---------

### Questions

How to make a statement into a yes/no question, either add `Est-ce que` or switch the order of the role and the verb.

    Tu aimes une table.             = You like the table. (statement)
    Aimes tu une table?             = You like the table? (question)
    Est-ce que tu aimes une table ? = You like the table? (question)
    
How to make a question that needs a detailed answer by starting with `Qu'est-ce`.
    
    Tu fais.                = You do.             (statement)
    Qu'est-ce que tu fais?  = What are you doing? (question)
    Tu aimes.               = You like.           (statement)
    Qu'est-ce que tu aimes? = What do you like?   (question)
    
Questioning words

    quel   = what (masculine)
    quelle = what (feminine)
    qui    = who
    quand  = when
    qù     = where
    
    
Simple question 

    is it? = est-ce que c'est?
    is it? = est-ce?
    it is  = c'est
    
Section 7
---------

### Ownership

The variations for the word `je`

    my = mon (singular masculine)
    my = ma  (singular femiine)
    my = mes (plural)
    
The variations for the word `tu`

    your = ton (singular masculine)
    your = ta  (singular femiine)
    your = tes (plural)
    
The variations for the word `il/elle`

    their = son (singular masculine)
    their = sa  (singular femiine)
    their = ses (plural)
    
The variations for the word `the`

    the = le  (masculine)
    the = la  (femiine)
    the = les (plural)
    
The variations for the word `to` (going to)

    to = a la (masculine)
    to = au   (femiine)
    to = aux  (plural)


And now, some examples

    Mon t-shirt  = My t-shirt
    Ma casquette = My cap
    Mes souliers = My shoes
    
    
Section 8
---------

### Some general vocab

    table        = une table
    sofa         = un sofa
    library      = la bibliothèque
    corner store = le dépanneur
    cigarette    = une cigarette
    bathroom     = la salle de bain
    home         = maison
    metro        = au metro
    bread        = les pains
    hockey       = le hockey
    food         = la nourriture
    sentence     = phrase
    movie        = la film
    never        = jamais
    always       = toujours
    in           = dans
    on           = sur
    every        = chaque
    tonight      = ce soir    
    
### Places
 
    Montreal = au Montrèal
    
### Nationality
    
    North American(m) = American du North
    North American(f) = Americane du North
    African(m)        = Africain
    African(f)        = Africaine
    Indian(m)         = Indien
    Indian(f)         = Indienne
