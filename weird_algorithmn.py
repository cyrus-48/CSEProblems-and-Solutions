# Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
# $$ 3 \rightarrow 10 \rightarrow 5 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1$$
# Your task is to simulate the execution of the algorithm for a given value of n.
# Input
# The only input line contains an integer n.
# Output
# Print a line that contains all values of n during the algorithm.
# Constraints

# 1 \le n \le 10^6

# Example
# Input:
# 3

# Output:
# 3 10 5 16 8 4 2 1


# also known as COllatz CAOnjecture of the "3n+1"  problem

"""
    . store numbers in a list (sequence)
    . while n != 1
        . if n is even : divide by 2
        . if n is odd : multiply by 3 and add 1 
        . Add each new number to the sequence
        

"""


def weird_algorithm(n:int)->str:
    """
    Time complexity : O(Log n)
    Space complexity O(k) where k is the number of steps
    
    """
    
    # initialize a list to store  the sequence 
    
    sequence  = [n]  # O(1) space for initial allocation
    
    while n != 1: # Number of iterations is the open problem in Collatz conjecture
        if n % 2 == 0:   # if n is even number 
            n = n // 2
            
        else:
            n = n* 3 + 1 # if n is old number 
            
        sequence.append(n) # O(1) per appedn operation
        
        
        
    return  ' '.join(map(str , sequence)) # O(k) space for fianl string 



n = int(input())
print(weird_algorithm(n))