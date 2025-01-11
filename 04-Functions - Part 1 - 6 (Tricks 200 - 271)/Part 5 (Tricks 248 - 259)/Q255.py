def func(x, y=2):
    num = 1
    for  i  in  range(y):
         num  =  num  *  x
    return num

print(func(4))
print(func(4, 4))