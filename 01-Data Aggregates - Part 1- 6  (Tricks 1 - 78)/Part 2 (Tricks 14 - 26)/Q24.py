data = {'one': 'two',  'two': 'three', 'three': 'one'}
res = data['three']

for k in range(len(data)):
    res = data[res]

print(res)