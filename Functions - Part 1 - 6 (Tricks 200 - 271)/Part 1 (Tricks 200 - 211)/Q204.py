def func(num):
    res = '*'
    for k in range(num):
        res += res
    return res


for x in func(2):
    print(x, end='')