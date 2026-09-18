class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        bracket_pairs = {"{": "}", "(": ")", "[": "]"}
        stack = []
        for i in range(len(s)):
            if s[i] in bracket_pairs.keys():
                stack.append(s[i])
            else:
                if stack:
                    bracket = stack.pop()
                    if s[i] != bracket_pairs[bracket]:
                        return False
                else:
                    return False
        return True if not stack else False