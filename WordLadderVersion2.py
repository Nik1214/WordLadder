from collections import deque
import re
import string
import time
class Word:
    def __init__(self, a, parent):
        self.word = a
        self.parent = parent
        
class wordSolver:
    def __init__(self):
        self.dictionary = set(open("words.txt", 'r').read().split('\n'))
        self.alphabetSet = (list(string.ascii_lowercase))
        self.repeats = set()
        self.pathExists = True

    def setStart(self, temp):
        self.start = Word(temp, None)
        self.repeats.clear()
        self.repeats.add(self.start.word)

    def setEnd(self, temp):
        self.end = temp
        
    def checkIfEnd(self,word):
        if(word.word == self.end):
            return True
        return False
    def getCounter(self):
        string = str(self.counter)
        return (self.counter)
    
    def findNextWords(self, word):
        possibleWords = []
        for i in range(0,6):
            for x in range(0,26):
                tempWord = word.word[:i] + self.alphabetSet[x] + word.word[i+1:]
                tempWord = tempWord[:6]
                if tempWord in self.dictionary and (not tempWord in self.repeats):
                    possibleWords.append(Word(tempWord,word))
                    self.repeats.add(tempWord)
        return possibleWords

    def wordPath(self, temp):
        if(self.pathExists == False):
            self.counter = "-"
            return 
        if not (temp.parent == None):
            self.counter = self.counter + 1
            self.wordPath(temp.parent)
            return self.counter
    
    def algorithm(self):
        q = deque()
        q.append(self.start)
        while (len(q) != 0):
            popped = q.popleft()
            if(self.checkIfEnd(popped)):
                return popped
            q.extend(self.findNextWords(popped))
        if(len(q) == 0):
            self.pathExists = False
            return self.end
            
inputWords = deque()
inputWords = deque(open("puzzlesA.txt", 'r').read().split("\n"))
node = wordSolver()
printer = open("solutions.txt",'w')
while(len(inputWords) > 0):
    tempString = inputWords.popleft()
    word1 = tempString[:6].strip()
    word2 = tempString[7:].strip()
    node.setStart(word1)
    node.setEnd(word2)
    startTime = time.time()
    tempWord = node.algorithm()
    node.counter = 0
    finalTime = (time.time() - startTime)
    node.wordPath(tempWord)
    numNodes = node.counter
    numNodes = str(numNodes)
    printer.write(word1 + " " + word2  + " " + numNodes +" " + str(finalTime) + '\n')
printer.close()
    

##startTime = time.time()
##temp = node.algorithm()
##finalTime = (time.time() - startTime)
##node.wordPath(temp)
##print(str(finalTime))


