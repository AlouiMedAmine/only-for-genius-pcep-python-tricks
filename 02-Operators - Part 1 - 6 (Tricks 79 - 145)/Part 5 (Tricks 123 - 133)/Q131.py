list1   =  ['Peter',  'Paul',  'Mary',  'Jane']
list2   =  ['Peter',  'Paul',  'Mary',  'Jane']

print(list1  is not  list2) #True
print(list1 != list2)     #False

list1  =  list2

print(list1 is not list2) #False
print(list1 != list2)     #False