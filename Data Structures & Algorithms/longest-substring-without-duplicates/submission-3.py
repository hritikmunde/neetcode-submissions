class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        hash_map = {}
        slow = 0
        fast = slow
        maxLen = 1
        while fast < len(s):
            while fast < len(s) and s[fast] not in hash_map:
                hash_map[s[fast]] = hash_map.get(s[fast], 0) + 1
                fast += 1
            maxLen = max(maxLen, fast - slow)
            hash_map[s[slow]] -= 1
            if hash_map[s[slow]] == 0:
                del hash_map[s[slow]]
            slow += 1
        return maxLen