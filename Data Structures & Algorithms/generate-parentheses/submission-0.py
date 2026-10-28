class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        string = ""
        res = []
        def backtrack(open_count, close_count):
            nonlocal string
            if len(string) == 2*n:
                res.append(string)
                return
            if open_count < n:
                string += "("
                backtrack(open_count + 1, close_count)
                string = string[:-1]
            if close_count < open_count:
                string += ")"
                backtrack(open_count, close_count + 1)
                string = string[:-1]
        backtrack(0, 0)
        return res