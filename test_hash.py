from hash import HashMap
import unittest

WORDLIST_FILENAME = "words.txt"

def loadWords(numWords):
    """
    Returns a list of valid words, strings of lowercase letters.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    counter = 0
    wordList = []
    while counter < numWords:
        for line in inFile:
            wordList.append(line.strip().lower())
            counter += 1
            break
    print(" ", len(wordList), "words loaded.")
    return wordList

def test_map_creation(num):
    print('Test Map creation...', end="")

    try:
        a = HashMap(num)
        print('Success')
        return a
    except:
        print('Failure')

def test_insert(map, wordList):
    print('Test Map insertions "a" to "z"...', end="")

    try:
        for word in wordList:
            map.insert(word, word)
        print('Success')
        print(map)
    except Exception as err:
        print('Failure: {}'.format(err))


def test_lookup(map, wordList):

    print('Test Map lookups "a" to "z"...', end="")

    try:
        for word in wordList:
            map.lookup(word)
        print('Success')
        print(map)
    except Exception as err:
        print('Failure: {}'.format(err))

def test_remove(map, wordList):

    print('Test Map removals "a" to "z"...', end="")

    try:
        for word in wordList:
            map.remove(word)
        print('Success')
        print(map)
    except Exception as err:
        print('Failure: {}'.format(err))

def test_empty(map):
    print('Map should be empty...', end="")
    try:
        for item in map:
            if item is not None:
                raise MapFailure('Failure')
        else:
            print('Success')
            print(map)
    except Exception as err:
        print('Failure: {}'.format(err))



while True:
    try:
        numBuckets = int(input('How many buckets to fill hash map?: '))
        numWords = int(input('How many words to load from wordList?: '))

        break
    except:
        print("Please enter a valid integer.")

wordList = loadWords(numWords)

def checkForErrors(wordList):
    print("Testing HashMap class")
    a = test_map_creation(numBuckets)
    test_insert(a, wordList)
    test_lookup(a, wordList)
    test_remove(a, wordList)

checkForErrors(wordList)