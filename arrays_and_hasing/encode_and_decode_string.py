from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "[]"
        first = True
        returnValue = "["
        for value in strs:
            if not first:
                returnValue += "#,"
            returnValue += '"'
            returnValue += value
            returnValue += '"'
            first = False
        returnValue += "]"
        return returnValue

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        s = s.replace("[", "")
        s = s.replace("]", "")
        s = s.replace('"', "")
        return s.split("#,")


solution = Solution()
encoded = solution.encode(["neet", "code", "love", "you"])
print(encoded)
decoded = solution.decode(encoded)
print(decoded)
