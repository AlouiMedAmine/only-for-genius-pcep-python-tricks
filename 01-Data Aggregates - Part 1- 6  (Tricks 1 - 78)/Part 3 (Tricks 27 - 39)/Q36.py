nums  =  [1,  2,  3]
data = ('Peter',) * (len(nums) - nums[::-1][0])
print(data)