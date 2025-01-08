data = [10, 2, 1, 7, 5, 6, 4, 3, 9, 8]


def find_high_low(nums):
    nums.sort()

    return nums[-1], nums[0]


high, low = find_high_low(data)

print(('The highest number is {} ' + 'and the lowest number is {}.').format(high, low))