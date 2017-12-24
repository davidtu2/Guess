'''
Author:     David Tu
Contact:    david.tu2@csu.fullerton.edu / 626-497-3531
MyPRNG.py:  Pseudo Random Number Generator(PRNG) Implementation
Input:      Integers of rseed, minimun and maximum
Output:     A random number within the range [min max)
'''
from time import time

class MyPRNG(object):
    z = 0#the seed
    min = 1
    max = 1000
    randomNumbers = []
    originalSeed = 0

    def __init__(self):
        for i in range(101):#initializting an array
            self.randomNumbers.append(0)

    def seed(self, rseed):
        if rseed == 0:
            self.z = int(time()) % 60#gets the time in sec
        else:
            self.z = rseed
        self.originalSeed = self.z

        for i in range(101):#populating the list of random numbers
            self.randomNumbers[i] = self.next_prn()
            self.z = self.randomNumbers[i]

    def next_prn(self):
       return 16807 * self.z % 2147483647# PRNG formula: (a * z) % m

    def answer(self):
        return (self.randomNumbers[100] % (self.max - self.min)) + self.min

    def setMin(self, minimum):
        self.min = minimum

    def setMax(self, maximum):
        self.max = maximum

    def displayRandomNumbers(self):
        print (self.randomNumbers)

    def getSeed(self):
        return self.originalSeed