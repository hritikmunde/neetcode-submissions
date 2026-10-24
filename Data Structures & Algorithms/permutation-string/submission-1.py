class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1
        n = len(s1)
        s2_map = {}
        for char in s2[:n]:
            s2_map[char] = s2_map.get(char, 0) + 1
        slow = 0
        fast = n
        while fast < len(s2):
            if s1_map == s2_map:
                return True
            s2_map[s2[fast]] = s2_map.get(s2[fast], 0) + 1
            fast += 1
            s2_map[s2[slow]] -= 1
            if s2_map[s2[slow]] == 0:
                del s2_map[s2[slow]]
            slow += 1
        return s1_map == s2_map