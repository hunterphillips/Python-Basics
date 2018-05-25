
# Index: return index of substr OR list item
print(['l', 'e'].index('e'))  # -> 1

# Sum: sum iterables (optional 'start' argument)
someSum = sum([1, 2, 3, 4, 5])

# List - new list of interable's items
print(list('new list'))  # -> ['n', 'e', 'w', ' ', 'l', 'i', 's', 't']

someList = ['junk', 'in', 3, 'trunk', True, {'key': 'value'}]
print(someList[1])
someList.append('more stuff')  # add 1 item to end of list
someList.extend(['more', 'stuff'])  # adds iterable item(s) to list
someList.remove(3)  # removes 1st matching value
del someList[2]  # removes At Specified index

# Sets -> unique collection, define with {} or set() function
unique_list = {'scissors', 3, False}
unique_list.add(3)  # prevents duplicates
print(unique_list)
unique_letters = set('abbacbcdcad')  # {'d', 'a', 'b', 'c'}
print('letters', unique_letters)

# Tuple -> immutable list
zoo = 'lion', 'zebra', 'rhino', 'flamingo'
# check if element exists
print('elephant' in zoo)  # False
# assigns variables for each tuple item
(leo, stripes, husk, bird) = zoo
print(leo)  # 'lion'
# convert to list / tuple
list(zoo)
tuple(zoo)

# Dictionairies -> ~ js objects
myDict = {'a': 1, 'b': 2, 'c': 3}
myDict['d'] = 4
print(myDict)
