def func(a=1, b=1, c=2):
    pass


"""

def func(a=1, b=1, c=2):         # Ok
    pass

def func(a=1, b=1, c=2, d):      # not ok
    pass

def func(a=1, b):                # not ok
    pass

def func(a=1, b, c=2):           # not ok
    pass


"""