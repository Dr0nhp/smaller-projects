import random

wordList = ["Sample","List"]
empty = []
choice = ""
deadInt = 7

def getword(wordList):
    word = random.choice(wordList)
    return word

def findOccurrences(word, choice):
    OcList = [i for i, letter in enumerate(word) if letter == choice]
    return OcList 

def createSample(OcList, empty, choice):
    if OcList:
        for x in enumerate(OcList):
            empty[x]= choice
    if not OcList:
        deathCount(deadInt)
    return empty

def deathCount(deadInt):
    deadInt = deadInt -1
    return deadInt




#def game (wordList, empty, choice, deadInt):
#    getword(wordList)
#    print ("test1")
#    findOccurrences(word, choice)
#    print ("test2")
#    createSample(OcList, empty, choice)
#    return 0