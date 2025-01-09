def test(x, y=23, z=10):
    print('x is  ', x, 'and y is  ', y, 'and z is  ', z)


test(3, 7)
test(42, z=24)
test(z=60, x=100)