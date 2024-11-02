"""
LeetCode#20
Given a string that only contains the characters (,), {,},[,], determine
if the input string is valid
"""

# Solution - 1
class ValidateParenthisis(object):
    def isValid(self,s):
        stack=[]
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack or (c==')' and stack[-1]!='(') or \
                (c=='}' and stack[-1]!='{') or\
                (c==']' and stack[-1]!='['):
                    return False
                stack.pop()
        return not stack

s = "({[]})"
print(ValidateParenthisis().isValid(s))  # True
s="()}{"
print(ValidateParenthisis().isValid(s))  # False

# Solution - 2

def isValid(s):
    stack = []
    pairs= {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    for bracket in s:
        if bracket in pairs:
            stack.append(bracket)
        elif len(stack) == 0 or \
        pairs[stack.pop()] != bracket:
            return False
        return len(stack) == 0
    s = "({[]})"
    print(isValid(s))  # True
    s="()}{"
    print(isValid(s))  # False

        