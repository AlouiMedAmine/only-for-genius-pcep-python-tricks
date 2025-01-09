def func1(a):
    return a ** a


def func2(a):
    return func1(a) * func1(a)


print(func2(2))