# Time: O(n²)
# Space: O(n)
# Best Time: O(n)
# Best Space: O(1)

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]
            answer.append(product)
        return answer
