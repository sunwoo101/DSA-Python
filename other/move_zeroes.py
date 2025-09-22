class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # print(nums)
        for i in range(len(nums) - 1):
            counter = 0
            while nums[i] == 0 and (i != len(nums) - 2 or nums[i] == 0 and nums[i + 1] != 0) and counter < len(nums):
                counter += 1
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j + 1]
                nums[-1] = 0
        print(nums)
