# Iterate through input
# If map of string arrays is emptym add the element to a new list in the map
# Check if map includes a key that equals sorted element, then add
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for value in strs:
            if map:
                if "".join(sorted(value)) in map:
                    map["".join(sorted(value))].append(value)
                else:
                    map["".join(sorted(value))] = [value]
            else:
                map["".join(sorted(value))] = [value]

        return list(map.values())


solution = Solution()
print(solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
