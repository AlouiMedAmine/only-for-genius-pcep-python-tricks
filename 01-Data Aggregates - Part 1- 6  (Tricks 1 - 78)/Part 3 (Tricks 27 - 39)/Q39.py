fruits1 = ['Apple', 'Pear', 'Banana']
fruits2 = fruits1
fruits3 = fruits1[:]

fruits2[0] = 'Cherry'
fruits3[1] = 'Orange'

res = 0
for i in (fruits1, fruits2, fruits3):
    if i[0] == 'Cherry':
        res += 1

    if i[1] == 'Orange':
        res += 10

print(res)