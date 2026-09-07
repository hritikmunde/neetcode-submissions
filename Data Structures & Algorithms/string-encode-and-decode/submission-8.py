class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "__EMPTY_STR__"
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}-{s}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "__EMPTY_STR__":
            return []
        decoded_strs = []
        i = 0
        while i < len(s):
            j = s.find("-", i)
            length = int(s[i:j])
            str_start = j + 1
            str_end = str_start+length
            decoded_strs.append(s[str_start:str_end])
            i = str_end
        return decoded_strs