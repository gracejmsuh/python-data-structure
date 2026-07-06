'''
When there is an unsorted array containing only positive values 
find the index of subarray that has the same value as S by adding values in the subarray. 
Index starts from 1.

Input: arr = [1, 2, 3, 7, 5], s = 12, Output: [2, 4]

Sum from index 2 to 4: 2 + 3 + 7 = 12
Input: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], s = 15, Output: [1, 5]
'''

# Method 1
# This one takes O(n^2) at most. 
def find_subarray(arr, s):
    for i in range(len(arr)):
        subtotal = 0
        for j in range(i, len(arr)):
            subtotal += arr[j]
            if subtotal == s:
                return [i+1, j+1]
    return [-1]

# Method 2 -> O(n)
def find_subarray2(arr, s):
    left = 0
    subtotal = 0

    # Move right pointer to the right one by one
    for right in range(len(arr)):
        subtotal += arr[right] # Add all values up to where right points at  
        
        # If subtotal is greater than s, subtrack value from the leftside of the array and increment left pointer one by one until the subtotal is smaller than s
        while left < right and subtotal > s:
            subtotal -= arr[left]
            left += 1

        # Return index if subtotal = s
        if subtotal == s:
            return [left+1, right+1] # +1 is must since it starts from 1(mentioned in the question)
    
    return [-1]    
        




sample1 = ([1, 2, 3, 7, 5], 12)
sample2 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)
for arr, s in (sample1, sample2):
    print(find_subarray2(arr, s))