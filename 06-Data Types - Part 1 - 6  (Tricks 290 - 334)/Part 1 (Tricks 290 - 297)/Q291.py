name  =  input('What is your name?')
sum  =  0
score  =  0
count  =  0
while score !=-1:
    score = int(input('Enter your scores: (-1 to end)'))
    if score == -1:
       break
    sum += score
    count += 1
average = sum/count
print('%-20s2 your average score  is: %4.1f' %(name,average))

