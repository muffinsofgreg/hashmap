from hash import HashMap

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words, strings of lowercase letters.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print(" ", len(wordList), "words loaded.")
    return wordList

print('Testing HashMap class')


def test_map_creation(num):
    print('Test Map creation...', end="")

    try:
        a = HashMap(num)
        print('Success')
        return a
    except:
        print('Failure')


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
#            't', 'u', 'v', 'w', 'x', 'y', 'z']

def test_insert(map, wordList):
    print('Test Map insertions "a" to "z"...', end="")

    try:
        for word in wordList:
            a.insert(word, word)
        print('Success')
        print(a)
    except:
        print('Failure')


def test_lookup(map, wordList):

    print('Test Map lookups "a" to "z"...', end="")

    try:
        for word in wordList:
            a.lookup(word)
        print('Success')
        print(a)
    except:
        print('Failure')

def test_remove(map, wordList):

    print('Test Map removals "a" to "z"...', end="")

    try:
        for word in wordList:
            a.remove(word)
        print('Success')
        print(a)
    except:
        print('Failure')

def test_empty(map):
    print('Map should be empty...', end="")
    try:
        for item in map:
            if item is not None:
                raise MapFailure('Failure')
        else:
            print('Success')
            print(a)
    except:
        print("Failure")


wordList = loadWords()
inputs = int(input('How many buckets to fill hash map?: '))

a = test_map_creation(inputs)

test_insert(a, wordList)
test_lookup(a, wordList)
test_remove(a, wordList)