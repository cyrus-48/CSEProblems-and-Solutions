# """
# Time limit: 1.00 s
# Memory limit: 512 MB



# You are given all numbers between 1,2,\ldots,n except one. Your task is to find the missing number.
# Input
# The first input line contains an integer n.
# The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
# Output
# Print the missing number.
# Constraints

# 2 \le n \le 2 \cdot 10^5

# Example
# Input:
# 5
# 2 3 1 5

# Output:
# 4

#


def find_missing_number(n:int, numbers: list[int])->int:
    """
    Time complexity : O(n)
    Space complexity O(1)
    
    """
    
    # The sum of the first n natural numbers is given by the formula n*(n+1)/2
    # The missing number can be found by subtracting the sum of the given numbers from the expected sum.
    
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    
    return expected_sum - actual_sum

n= int(input())
numbers = list(map(int, input().split()))

print(find_missing_number(n, numbers))