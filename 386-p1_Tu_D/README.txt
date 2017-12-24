AUTHOR: David Tu
CONTACT: david.tu2@csu.fullerton.edu / 626-497-3531

BUGS: No known bugs
FEATURES: No additional features added
COMPLETED: Guessing Game and MyPRNG implementation
NOT COMPLETED: N/A
HOW TO USE THE PROGRAM:
	Pre-Requisite(s)/External Dependencies:
		MyPRNG.py is also included in the diretory of guess.py
		Installation of Phyton 3.4 or higher
	
	Please note that these directions are for Win10:
	1. While in the command prompt, type the following: phyton guess.py
    	Where 'phyton' is the directory of your phyton.exe and 'guess.py' is the directory of your copy of guess.py
    	2. Following the command, these optional parameters may be included:
    		-h 		Prints out a help message
    		-v 		Turn on debugging messages
    		-s seed 	Sets the seed for the PRNG
    		-n minimum 	Sets the min of the range of numbers that program will select from
    		-x maximum 	Sets the max of the range of numbers that program will select from
    	The following is an example of executing the program while enabling help messages and setting the seed to 2: 
		C:\Python34\python.exe C:\guess.py -h -s 2
	3. The Guessing Game will start and from there, the player can play the game by inputing numbers as their 'guess'
	4. If the player wants to exit, they can simply input 0 anytime the game asks for a number to quit