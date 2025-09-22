class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = dict()
        for value in s:
            if value in s_map:
                s_map[value] += 1
            else:
                s_map[value] = 1
        print(s_map)
        count = len(s_map)
        for value in t:
            print(value)
            if value in s_map:
                s_map[value] -= 1
                if s_map[value] == 0:
                    count -= 1
            else:
                return False
        print(s_map)
        print(count)

        if count == 0:
            return True
        return False


solution = Solution()
print(solution.isAnagram("ajar", "jraa"))
