data = {}

def func(d, key, value):
    d[key] = value

print(func(data, '1', 'Peter'))

"""

func is a void (ie: doesn't have a return statement), 
returns the None object. 

Many in-built functions like print() are void and return None.

"""