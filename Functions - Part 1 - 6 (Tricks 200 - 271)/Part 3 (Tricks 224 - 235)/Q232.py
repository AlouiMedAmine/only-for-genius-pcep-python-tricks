def func(data):
    data = [7, 23, 42]
    print('Function scope: ', data)


data = ['Peter', 'Paul', 'Mary']
func(data)
print('Outer scope: ', data)