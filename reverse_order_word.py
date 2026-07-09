'''
Write a function that returns the given string in reverse order 

Input: s = “aircraft”
Output: “tfarcria”
'''

class Stack:
    def __init__(self):
        # Prepare list to store data 
        self.items = []
    
    '''
    Add value in the stack 
    O(1) -> Insert new value at the end of stack, no need to shift other element in the stack 
    '''
    def push(self, val):
        self.items.append(val)
    
    '''
    Delete/pop the top value in the stack 
    O(1) -> Remove a value from the end of stack, no need to shift other element in the stack 
    '''
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print('Stack is empty')
    
    '''
    Return the top value in the stack 
    O(1) -> We can directly access to the value that is on top of the stack 
    '''
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print('Stack is empty')
    
    '''
    Return how many items in the stack 
    O(1) 
    '''
    def __len__(self):
        return len(self.items)

'''
Put each character in the stack in order. 
Once it pushes the last character, it starts to pop each one out. (reverse order)
O(n) -> Going through the string of length n twice when pushing all characters onto the stack, and to pop them off 
--> Growing linearly with the input size
'''
def reverse_word(word):
    S = Stack()
    answer = ''
    
    for w in word:
        S.push(w)
    while len(S) > 0:
        answer += S.pop()
    return answer


print(reverse_word("aircraft"))