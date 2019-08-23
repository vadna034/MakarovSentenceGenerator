import pickle
import random
import re

class Word:
    def __init__(self, inputString):
        self.key = inputString
        self.nextWords = {}
        self.numWords = 0

    def addWord(self, addNext):
        assert isinstance(addNext, str)
        if addNext in self.nextWords:
            self.nextWords[addNext] += 1
            self.numWords += 1
        else:
            self.nextWords[addNext] = 1
            self.numWords += 1

    def getNext(self):
        x = random.randint(1, self.numWords)
        sum = 0
        for word in self.nextWords:
            sum += self.nextWords[word]
            if sum >= x:
                return word

    def __eq__(self, other):
        if isinstance(other, str):
            return other == self.key
        elif isinstance(other, Word):
            return other.key == self.key
        else:
            return False

    def __str__(self):
        return self.key + ': ' + str(self.nextWords)

class wordContainer:
    def __init__(self):
        self.allWords = []
        self.sentenceStarters = {}
        self.numStarters = 0

    def addSentenceStarter(self, nextWord):
        self.numStarters += 1
        if nextWord in self.sentenceStarters:
            self.sentenceStarters[nextWord] += 1
        else:
            self.sentenceStarters[nextWord] = 1

    def addWord(self, firstWord, nextWord):
        if bool(re.search('[.?!]"?', firstWord)) and firstWord!='St.' and nextWord[0].isupper():
            self.addSentenceStarter(nextWord)
            if firstWord in self.allWords:
                index = self.allWords.index(firstWord)
                self.allWords[index].addWord('')
            else:
                self.allWords.append(Word(firstWord))
                self.allWords[-1].addWord('')
        else:
            if firstWord in self.allWords:
                index = self.allWords.index(firstWord)
                self.allWords[index].addWord(nextWord)
            else:
                self.allWords.append(Word(firstWord))
                self.allWords[-1].addWord(nextWord)

    def getWord(self, inputWord):
        index = self.allWords.index(inputWord)
        return self.allWords[index]

    def getSentenceStarter(self):
        x = random.randint(1, self.numStarters)
        sum = 0
        for word in self.sentenceStarters:
            sum += self.sentenceStarters[word]
            if sum >= x:
                return word

    def generateSentence(self):
        sentenceString = ""
        starter = self.getSentenceStarter()
        sentenceString += starter

        while not bool(re.search('[.?!]"?', starter)) and starter!='St.':
            index = self.allWords.index(starter)
            thisWord = self.allWords[index]
            starter = thisWord.getNext()
            sentenceString = sentenceString + ' ' + starter

        if sentenceString[-1] == '"':
            sentenceString = '"' + sentenceString
        if sentenceString[-1] == '\'':
            sentenceString = '\'' + sentenceString
        return sentenceString

    def __str__(self):
        exampleString = 'All words: ['
        for word in self.allWords:
            exampleString = exampleString + word.key + ', '
        exampleString = exampleString[:-2] + '}\n'

        exampleString += 'Sentence Starters: {'
        for word in self.sentenceStarters:
            exampleString += "'" + word + "': " + str(self.sentenceStarters[word]) + ','
        exampleString = exampleString[:-1] + '}' + '\n'
        return exampleString

f = open('obj.pck1', 'rb')
obj = pickle.load(f)
f.close()
Story = ""
for i in range(10):
    Story += obj.generateSentence() + " \n"

print(Story)