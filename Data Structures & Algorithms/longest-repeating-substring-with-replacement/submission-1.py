class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        slow = 0
        maxReplacement = 0
        for fast in range(len(s)):
            frequency[s[fast]] = frequency.get(s[fast], 0) + 1
            while (fast - slow + 1) - max(frequency.values()) > k and slow < len(s):
                frequency[s[slow]] -= 1
                slow += 1
            maxReplacement = max(maxReplacement, (fast - slow + 1))
        return maxReplacement
