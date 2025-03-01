def second_largest(nums):
    if len(nums) < 2:
        return None  # Not enough elements
    
    first, second = float('-inf'), float('-inf')
    
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    
    return second if second != float('-inf') else None
numbers = [15, 42, 78, 23, 56, 89, 99, 99, 65]
result = second_largest(numbers)
print("Second largest number:", result)
