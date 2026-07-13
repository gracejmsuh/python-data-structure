'''
N people, numbered 1 to N, are seated in a circle, and a positive integer K (≤ N) is given. 
Starting from the beginning, the K-th person is removed. 
Once a person is removed, the process continues along the circle formed by the remaining people. 
This process repeats until all N people have been removed.
'''

from collections import deque

def josephus(n, k):
    # deque that has numbers from 1 to N
    dq = deque(range(1, n+1))
    result = []

    # Repeat until there is an item/person in deque
    while dq:
        # Move k-1 items from front to the back(left -> right) 
        dq.rotate(-(k-1))
        # Remove Kth item
        result.append(dq.popleft())

    return result