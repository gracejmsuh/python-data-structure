'''
Find the two largest number in the array and return those two number in list format. 
input: [3, -1, 5, 0, 7, 4, 9, 1], output: [9, 7]
input: [7], output: [7]

Big O: O(n) -> Iterate through the array only once where there are n elements in the array
'''


def max_num(arr):
    if len(arr) < 2: # Return the array when there is only one element or none
        return arr

    max1 = arr[0]
    max2 = arr[1]

    if max2 > max1:
        max1, max2 = max2, max1

    for i in arr[2:]:
        if i > max1:
            max1, max2 = i, max1 # Need to set max2 to max1, otherwise max2 doesn't get updated 
        elif i > max2:
            max2 = i

    return [max1, max2]

    
#Test
arr = [[3, -1, 5, 0, 7, 4, 9, 1], [7]] # Expected: [9, 7] and [7]
for a in arr:
    print(f"Largest number from {a}: {max_num(a)}")