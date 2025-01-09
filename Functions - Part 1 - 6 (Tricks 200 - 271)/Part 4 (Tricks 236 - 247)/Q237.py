def function_1(a):
    return None

def function_2(a):
    return function_1(a) * function_1(a)

print(function_2(2))


""" 
will cause a runtime error
==> TypeError: unsupported operand type(s) for *:
'NoneType' and 'NoneType'

"""
