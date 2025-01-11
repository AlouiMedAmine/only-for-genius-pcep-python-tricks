def func(n):
    s  =  '*'
    for  i  in range(n):
         s +=  s
    yield  s


for  x  in  func(2):
     print(x,  end='')