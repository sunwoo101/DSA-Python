# Time: O(n)
# Space: O(n)
# Best Time: O(n)
# Best Space: O(n)

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checked_set = set()
        nums_set = set()
        max_count = 0
        for value in nums:
            nums_set.add(value)

        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set and nums[i] not in checked_set:
                checked_set.add(nums[i])
                n = nums[i] + 1
                count = 1
                stop = False
                while not stop:
                    if n in nums_set:
                        count += 1
                        checked_set.add(n)
                    else:
                        stop = True
                    n += 1

                if count > max_count:
                    max_count = count

        return max_count


solution = Solution()
result = solution.longestConsecutive([2, 20, 4, 10, 3, 4, 5])
print(result)

result = solution.longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1])
print(result)
