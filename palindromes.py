'''
Return True if given string is palindrome, otherwise return False.

Input: madam, Output: True
Input: tomato, Output: False
'''

def is_palindrome(word):
    left = 0 # Leftmost char in the word
    right = len(word) - 1 # Rightmost char in the word

    while left < right:
        if word[left] != word[right]: # Comparison, if there is difference return False and done
            return False
        left = left + 1
        right = right -1
    return True # If it makes it til end, return True(palindrome)

# More effective way
def is_palindrome2(word):
    # Generate word in reverse order and compare it to original word, return True if they are the same. Otherwise, return False
    return word == word[::-1]



words = ["racecar", "rotor", "tomato", "별똥별", "코끼리"]
for word in words:
    print(f"Is '{word}' palindrome?  {is_palindrome2(word)}")