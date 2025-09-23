from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            nums_map[str(nums[i])] = i

        i = 0
        for value in nums:
            if str(target - int(value)) in nums_map:
                if nums_map[str(target - int(value))] != i:
                    if i < (nums_map[str(target - int(value))]):
                        return [i, nums_map[str(target - int(value))]]
                    return [nums_map[str(target - int(value))], i]
            i += 1
