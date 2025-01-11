x = 42

def func():
    global x
    print('1.  x: ', x)
    x = 23
    print('2. x: ', x)


    func()
    print('3. x: ', x)