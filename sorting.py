'''
Sort array when there are only 0s and 1s in ascending order. 

Input: [1, 0, 1, 1, 1, 1, 1, 0, 0, 0], Output: [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
Input: [1, 1], Output: [1, 1]
'''

def is_ascending(arr):
    arr.sort()

# Different method 
def sort_array(arr):
    left = 0 # Index 0
    right = len(arr) - 1 # Last index of arr

    while left < right:
        # Move left pointer until it encounters 1
        while left < len(arr) and arr[left] == 0: # the value needs to be 0, not left = 0
            left += 1
    
        # Move right pointer until it encounters 0
        while right > 0 and arr[right] == 1: # the value needs to be 1, not left = 1
            right -= 1
    
        # If they are not met, switch 0 and 1
        if left < right:
            arr[left], arr[right] = 0, 1
            left += 1
            right -= 1


for arr in ([1, 0, 1, 1, 1, 1, 1, 0, 0, 0], [1, 1]):  
    sort_array(arr)  
    print(arr)