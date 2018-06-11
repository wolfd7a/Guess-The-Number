import random
import sys

def WrongValue() :
    print('The entered value should be an integer.')

def RaiseException() :
    print("I did not understand you're answer")

def ProgramEnd() :
    sys.exit(0)

def GoAgain() :
    restart = input('Do you want to play again ?')
    if restart in ('yes','Yes','yEs','yeS','YEs','yES','YeS','YES') :
        GuessTheNumber()
    elif restart in ('no','No','nO','NO') :
        ProgramEnd()
    else :
        RaiseException()
        GoAgain()

def GuessTheNumber() :
    ComputerNumber  = random.randint(1, 50)
    choice=0
    while choice==0 :
        Guess = input("What number did I just think about ?")
        try :
            int(Guess)
            choice=1
            break
        except :
            WrongValue()
    while Guess!= ComputerNumber :
        if Guess > ComputerNumber :
                print('Lower')
                GuessTheNumber()
        else :
            print('Higher !')
            GuessTheNumber()
    print('You got it !')
    GoAgain()

GuessTheNumber()
