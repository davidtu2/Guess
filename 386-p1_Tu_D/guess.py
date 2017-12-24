'''
Author:         David Tu
Contact:        david.tu2@csu.fullerton.edu / 626-497-3531
guess.py:       Guessing Game Implementation: Provides gameplay where the player has to guess a number
    Input:      Optionally, Integers of rseed, mini and maxi upon startup. During gameplay, numbers are only accepted
    Output:     None
'''
from MyPRNG import MyPRNG
import sys, getopt

def main(argv):
    debug = False
    rseed = 0
    mini = 1
    maxi = 1000

    try:
        opts, args = getopt.getopt(argv, "hvs:n:x:", ["help", "debug", "seed=", "min=", "max="])#the ":" and "=" signs indicate that they require input
    except getopt.GetoptError:
        print("ARGUMENT ERROR")
        usage()
        exit(-1)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()#help message
        elif opt in ("-v", "--debug"):
            print("DEBUG MODE IS TURNED ON")
            debug = True
        elif opt in ("-s", "--seed"):
            rseed = int(arg)#update the seed
        elif opt in ("-n","--min"):
            mini = int(arg)#update the minimum
        elif opt in ("-x","--max"):
            maxi = int(arg)#update the maximum

    gen = MyPRNG()
    gen.setMin(mini)
    gen.setMax(maxi)
    gen.seed(rseed)#If rseed isn't updated, it will default to seconds from time
    a = gen.answer()#get the answer for comparing

    if debug == True:
        print("SEED: ", gen.getSeed())
        print("MIN: ", mini)
        print("MAX: ", maxi)
        print("THE PRNG NUMBERS ARE, USING (A * Z) % M, where A = 7^5, M = 2^31 - 1, AND Z IS THE SEED: ")
        gen.displayRandomNumbers()
        print("THE ANSWER IS:", a, "(THE 100th PRNG NUMBER % (MAX - MIN) + MIN)")

    try:
        guess1 = int(input("Welcome to Guess a Number! I'm thinking of a number, guess what it is!"))
    except:
        print("INVALID INPUT ERROR. PLEASE INPUT ONLY NUMBERS")
        input("Press ENTER to exit")
        exit(-1)

    if guess1 == 0:
        input("Press ENTER to exit")
        exit(0)
    elif guess1 == a:
        print ("Your first guess was: " + str(guess1) + ". You Won! Congrats! :)")
        input("Press ENTER to exit")
        exit(0)
    else:
        try:
            guess2 = int(input("Your first guess was: " + str(guess1) + ". Wrong! Try again!"))
        except:
            print("INVALID INPUT ERROR. PLEASE INPUT ONLY NUMBERS")
            input("Press ENTER to exit")
            exit(-1)
     
    while True:#infinite loop until the player chooses the correct answer, or decides to exit
        if guess2 == 0:
            input("Press ENTER to exit")
            exit(0)
        elif guess2 == a:
            print ("Your next guess was: " + str(guess2) + ". You Won! Congrats! :)")
            input("Press ENTER to exit")
            exit(0)
        elif abs(a - guess2) < abs(a - guess1):#if the 2nd guess' distance to the answer is shorter than the 1st's
            guess1 = guess2
            try:
                guess2 = int(input("Your next guess was: " + str(guess2) + ", you are getting warmer!"))
            except:
                print("INVALID INPUT ERROR. PLEASE INPUT ONLY NUMBERS")
                input("Press ENTER to exit")
                exit(-1)
        elif abs(a - guess2) > abs(a - guess1):#if the 2nd guess' distance to the answer is further than the 1st's
            guess1 = guess2
            try:
                guess2 = int(input("Your next guess was: " + str(guess2) + ", you are getting colder!"))
            except:
                print("INVALID INPUT ERROR. PLEASE INPUT ONLY NUMBERS")
                input("Press ENTER to exit")
                exit(-1)
        else:#if the distances to the answer is the same for both guesses
            if guess2 == guess1:
                guess1 = guess2
                try:
                    guess2 = int(input("Your next guess was: " + str(guess2) + ". Why did you guess the same number? Try again!"))
                except:
                    print("INVALID INPUT ERROR. PLEASE INPUT ONLY NUMBERS")
                    input("Press ENTER to exit")
                    exit(-1)
            else:
                guess1 = guess2
                try:
                    #guess2 = int(input("Your next guess was: " + str(guess2) + ", but nothing changed. Try again!"))#Note: code commented out due to email: "If prev and current deltas are equal, tell player any answer (eg, "warmer")"
                    guess2 = int(input("Your next guess was: " + str(guess2) + ", you are getting warmer!"))
                except:
                    print("INVALID INPUT ERROR. PLEASE INPUT ONLY NUMBERS")
                    input("Press ENTER to exit")
                    exit(-1)

def usage():
    print("PROGRAM DESCRIPTION:    NUMBER GUESSING GAME WHICH UTILIZES A PSEUDO RANDOM NUMBER GENERATOR(PRNG) TO DETERMINE THE ANSWER")
    print("HOW TO RUN THE PROGRAM: WHILE IN COMMAND PROMPT, TYPE THE FOLLOWING: phyton guess.py")
    print("                        WHERE phyton IS THE DIRECTORY OF YOUR PHYTON.EXE AND guess.py IS THE DIRECTORY OF YOUR COPY OF GUESS.PY")
    print("                        FOLLOWING THE COMMAND, OPTIONAL PARAMATERS MAY BE INCLUDED:")
    print("-h                      PRINTS OUT A HELP MESSAGE")
    print("-v                      TURN ON DEBUGGING MESSAGES")
    print("-s seed                 SET SEED FOR THE PRNG")
    print("-n minimum              SETS THE MINIMUM FOR THE RANGE OF NUMBERS THE PROGRAM WILL SELECT FROM")
    print("-x maximum              SETS THE MAXIMUM FOR THE RANGE OF NUMBERS THE PROGRAM WILL SELECT FROM")
    print("THE FOLLOWING IS AN EXAMPLE OF EXECUTING THIS PROGRAM WHILE ENABLING HELP MESSAGES AND SETTING THE SEED TO 2: C:\Python34\python.exe C:\guess.py -h -s 2")
    print("PLEASE ALSO ENSURE THAT PRIOR TO EXECUTING THE SCRIPT THAT MyPRNG.py IS ALSO INCLUDED IN THE DIRECTORY OF guess.py")

if __name__ == "__main__":#if the python interpreter is running this module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__"
    main(sys.argv[1:])