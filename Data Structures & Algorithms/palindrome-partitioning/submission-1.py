class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            if start > len(s):
                return
            for i in range(start, len(s)):
                if self.isPalindrome(s, start, i):
                    path.append(s[start: i + 1])
                    backtrack(i + 1, path)
                    path.pop()
        backtrack(0, [])
        return res

    def isPalindrome(self, s, lo, hi):
        while lo <= hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True