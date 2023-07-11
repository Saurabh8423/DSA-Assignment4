def sortedSquares(nums):
    squared_nums = []
    for num in nums:
        squared_nums.append(num ** 2)
    
    squared_nums.sort()
    return squared_nums
nums = [-4, -1, 0, 3, 10]
result = sortedSquares(nums)
print(result)
