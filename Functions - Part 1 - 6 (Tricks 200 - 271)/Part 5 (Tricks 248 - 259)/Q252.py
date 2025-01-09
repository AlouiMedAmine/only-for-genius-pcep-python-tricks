"""
Q252: Select the true statement:


Answer: Keyword arguments cannot be
followed by positional arguments.


def func(a=1, b=1, c=2):         # Ok
    pass

def func(a=1, b=1, c=2, d):      # not ok
    pass

def func(a=1, b):                # not ok
    pass

def func(a=1, b, c=2):           # not ok
    pass


"""