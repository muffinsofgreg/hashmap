from hash import HashMap

a = HashMap(3)

a.insert('a', 1)
a.insert('b', 2)
a.insert('d', 4)

print(a)

# a.remove('a')
# a.remove('d')
# a.remove('f')

a.remove('d')

print(a)