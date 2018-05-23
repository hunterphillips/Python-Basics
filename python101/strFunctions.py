# Capitalize
myStr = 'Hello World'
print(myStr.capitalize())  # returns 'Hello world'

# Swap case: returns str with swap cased characters
print(myStr.swapcase())  # -> 'hELLO wORLD'

# Length
print(len(myStr))

# Replace: replace (target, newValue)
print(myStr.replace('World', 'errbody'))  # -> 'Hello errbody'

# Count: count occurrences of substr
print(myStr.count('l'))

# Startswith / Endswith
# returns boolean for matching str, optional 'start', 'end'
print(myStr.startswith('Hel'))
print(myStr.endswith('orld'))

# Split: returns list of str words, default splits on whitespace
print(myStr.split())

# Find: return index of substr, optional 'start', 'end'
print(myStr.find('W'))

# Is Alphanumeric (abc123) / Is Alphabetic (abc) / Is Numeric
print('1239406djeh'.isalnum())  # -> True
print('1239406djeh'.isalpha())  # -> False
print('1239406'.isnumeric())  # -> True
