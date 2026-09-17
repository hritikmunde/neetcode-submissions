class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = "".join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(phrase)-1
        while i <= j:
            if phrase[i] != phrase[j]:
                return False
            i += 1
            j -= 1
        return True