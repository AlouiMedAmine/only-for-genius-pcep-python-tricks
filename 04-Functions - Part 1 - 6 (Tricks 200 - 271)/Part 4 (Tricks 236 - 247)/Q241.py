data = 'abcdefg'

def func(text):
    del text[2]
    return text

print(func(data))