str1 = 'Peter'
str2 = str1[:]
print(str1 == str2) #True (some content)
print(str1 is str2) #True  #same memory location
print(id(str1), id(str2))  #same memory location