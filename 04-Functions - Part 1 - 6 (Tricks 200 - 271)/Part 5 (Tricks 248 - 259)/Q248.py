def func(x, y):
    if x == y:
        return x
    else:
        return func(x, y - 1)


print(func(0, 3))
