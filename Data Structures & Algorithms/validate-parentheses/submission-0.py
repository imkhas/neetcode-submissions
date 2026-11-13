class Solution:
    def isValid(self, s: str) -> bool:
        #Use stack since it is a stack problem
        stack = []

        closeToOpen = { ")" : "(" , "]" : "[" , "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1]  == closeToOpen[c]:
                    stack.pop() #Remove stack
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        
        