# Open a file / Creates new file if doesn't exist
# open in 'w'riting mode
fo = open('test.txt', 'w')

# Get file info
print('Name:', fo.name)  # -> test.text
# check if closed
print(fo.closed)  # -> False

# Write to file
fo.write('Written by the file.py file')
# Close file
fo.close()

fo = open('test.json', 'w')
fo.write('{"from": "file.py"}')

# Open in 'append' mode
fo = open('test.txt', 'a')
fo.write('\nmore stuff from file.py')

# Read from file
fo = open('test.txt', 'r+')
text = fo.read(10)  # (first 10 characters)
print(text)


# import data from csv file without numpy/pandas
import csv


# function to read/set data from 'filename' using delimiter 'd'
def open_with_csv(filename, d='\t'):
    data = []
    with open(filename, encoding='utf-8') as tsvin:
        data_reader = csv.reader(tsvin, delimiter=d)
        # loop over each line in data file
        for line in data_reader:
            data.append(line)
    return data


data_from_csv = open_with_csv('data.csv')
print(data_from_csv[0])
