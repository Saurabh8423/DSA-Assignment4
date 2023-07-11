def arrangeCoins(n):
    left, right = 0, n
    
    while left <= right:
        mid = (left + right) // 2
        total_coins = (mid * (mid + 1)) // 2
        
        if total_coins > n:
            right = mid - 1
        else:
            left = mid + 1
    
    return right
n = 8
result = arrangeCoins(n)
print(result)