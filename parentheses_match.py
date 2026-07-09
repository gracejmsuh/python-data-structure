'''
If parnetheses are matching(e.g. ( ) ), return True. Otherwise, return False. 
Only use ()

Input: ((a*(b+c))-d) / e 
Output: True

Input: (((a*(b+c))-d) / e
Output: False
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


def matching_parentheses(expression):
    S = Stack()
    for i in expression:
        if i == '(':
            S.push(i)
        elif i == ')':
            if len(S) == 0:
                return False
            S.pop()
        else:
            pass
    
    if len(S) == 0:
        return True
    else:
        return False 
    

print(matching_parentheses("((a * (b + c)) - d) / e"))
print(matching_parentheses("(((a * (b + c)) - d) / e"))