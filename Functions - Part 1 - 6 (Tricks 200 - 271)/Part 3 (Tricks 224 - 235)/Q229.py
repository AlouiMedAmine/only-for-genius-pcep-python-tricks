def func(n):
    s =  ''
    for i  in  range(n):
        s +=  '*'
        yield  s

for  x  in  func(3):
     print(x,  end='')