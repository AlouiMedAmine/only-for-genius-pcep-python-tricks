data =  { }
data[1] = 1
data['1'] = 2
data[1.0] = 4  #override data[1] = 1


#print(data) #
res = 0
for d in data:
    #print(data[d])
    res += data[d]

print(res)