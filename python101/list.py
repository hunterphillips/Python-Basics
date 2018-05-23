
# Index: return index of substr OR list item
print(['l', 'e'].index('e'))  # -> 1

# Sum: sum iterables (optional 'start' argument)
someSum = sum([1, 2, 3, 4, 5])

# List - new list of interable's items
print(list('new list'))  # -> ['n', 'e', 'w', ' ', 'l', 'i', 's', 't']

someList = ['junk', 'in', 3, 'trunk', True, {'key': 'value'}]
print(someList[1])
someList.append('more stuff')

# Sets -> unique collection
unique_list = {'scissors', 3, False}
unique_list.add(3)  # prevents duplicates
print(unique_list)

# tuple -> immutable list
t = 'dog', 'cat', 'fish'
print(t)
list_t = list(t)  # turn into List
print(list_t)

# Dictionairies -> ~ js objects
myDict = {'a': 1, 'b': 2, 'c': 3}
myDict['d'] = 4
print(myDict)
