
people = ['John', 'sarah', 'Bill', 'Joe']
# for loop
# for person in people:
#   print('Current Person', person)

# index interation
for i in range(len(people)):
  print('Current Person', people[i])
# lowerbound -> (exclude)upperbound, 0 - 9
for i in range(0, 10): 
  print(i)

# while 
count = 0
while count < 10: 
  print(count)
  if count == 5:
    break
  count += 1