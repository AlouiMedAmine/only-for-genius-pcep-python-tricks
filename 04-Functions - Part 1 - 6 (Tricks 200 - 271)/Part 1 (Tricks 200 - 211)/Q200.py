def func(data):
    for  d  in  data[::2] :
         yield d

for  x  in  func('abcdef'):
     print(x,  end='')