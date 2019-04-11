from hash import HashMap

WORDLIST_FILENAME = "words.txt"


def loadWords(numWords):
    """
    Returns list of valid words, strings of lowercase letters.
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
    inFile.close()
    return wordList


def checkMapSize(test_map):
    """
    Returns: int; size of map
    """
    try:
        counter = 0
        for line in test_map:
            if isinstance(line, list):
                for item in line:
                    counter += 1
            elif isinstance(line, tuple):
                counter += 1
            else:
                counter += 1
        return counter
    except Exception as err:
        print("Failure: {}".format(err))


def testMapCreation(num):
    print('Test Map creation...', end="")
    try:
        a = HashMap(num)
        print('Success')
        return a
    except Exception as err:
        print(f'Failure: {err}')


def testInsert(test_map, wordList):
    print('Test Map insertions from wordList...', end="")
    try:
        for word in wordList:
            test_map.insert(word, word)
        print('Success')

    except Exception as err:
        print(f'Failure: {err}')

    print("Test map size after insertions...", end="")
    try:
        if checkMapSize(test_map) == len(wordList):
            print("Success")
    except Exception as err:
        print(f"Failure, {err}")


def testLookup(test_map, wordList):

    print('Test Map lookups "a" to "z"...', end="")

    try:
        for word in wordList:
            test_map.lookup(word)
        print('Success')
    except Exception as err:
        print(f'Failure: {err}')


def testRemove(test_map, wordList):

    print('Test Map removals "a" to "z"...', end="")

    try:
        for word in wordList:
            test_map.remove(word)
        print('Success')
    except Exception as err:
        print(f'Failure: {err}')


def testEmpty(test_map, numBuckets):
    print('Map should be empty...', end="")
    try:
        for item in test_map:
            if item is not None:
                print("Failure, map is not empty")
                break
        else:
            print("Success")
    except Exception as err:
        print(f'Failure: {err}')

    print("Test map size after deletions...", end="")
    try:
        if checkMapSize(test_map) == numBuckets:
            print("Success")
    except Exception as err:
        print(f"Failure: {err}")


def check_all():
    while True:
        try:
            numBuckets = int(input('How many buckets to fill hash map?: '))
            numWords = int(input('How many words to load from wordList?: '))
            break
        except Exception as err:
            print(f"Please enter a valid integer: {err}")

    wordList = loadWords(numWords)

    def checkForErrors():
        print("Testing HashMap class")
        a = testMapCreation(numBuckets)
        testInsert(a, wordList)
        testLookup(a, wordList)
        testRemove(a, wordList)
        testEmpty(a, numBuckets)

    checkForErrors()


if __name__ == "__main__":
    check_all()
