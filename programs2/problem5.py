# Valid Parentheses Using a Stack
'''An online code editor checks whether brackets are balanced before a student submits
code.
Given a string containing the brackets (), [], and {}, determine whether every opening
bracket is closed by the same type of bracket in the correct order.'''


s = input("Enter the brackets: ")
stack = []
pairs = {')': '(', ']': '[', '}': '{'}

for bracket in s:
    if bracket in '([{':
        stack.append(bracket)
    else:
        if not stack or stack[-1] != pairs[bracket]:
            print(False)
            break
        stack.pop()
else:
    print(len(stack) == 0)
