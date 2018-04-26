from hash import HashMap

print('Testing HashMap class')

def test_map_creation(num):
    print('Test Map creation...', end="")

    try:
        a = HashMap(num)
        print('Success')
        return a
    except:
        print('Failure')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

def test_insert(map):
    print('Test Map insertions "a" to "z"...', end="")

    try:
        for letter in alphabet:
            a.insert(letter, letter)
        print('Success')
        print(a)
    except:
        print('Failure')


def test_lookup(map):

    print('Test Map lookups "a" to "z"...', end="")

    try:
        for letter in alphabet:
            a.lookup(letter)
        print('Success')
        print(a)
    except:
        print('Failure')

def test_remove(map):

    print('Test Map removals "a" to "z"...', end="")

    try:
        for letter in alphabet:
            a.remove(letter)
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


inputs = int(input('How many buckets to fill hash map?: '))

a = test_map_creation(inputs)

test_insert(a)
test_lookup(a)
test_remove(a)