class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {"{": "}", "(": ")", "[": "]"}
        stack = []
        for c in s:
            if c in bracket_pairs.keys():
                stack.append(c)
                
            else:
                if stack and c == bracket_pairs[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False