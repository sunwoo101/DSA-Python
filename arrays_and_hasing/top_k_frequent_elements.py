from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for value in nums:
            if value in map:
                map[value] += 1
            else:
                map[value] = 0

        sorted_list = list(sorted(map, key=map.get))
        sorted_list.reverse()
        answer = []
        for i in range(k):
            answer.append(sorted_list[i])

        return answer


solution = Solution()
print(solution.topKFrequent(nums=[1, 2, 2, 3, 3, 3], k=2))
print(solution.topKFrequent(nums=[7, 7], k=1))
