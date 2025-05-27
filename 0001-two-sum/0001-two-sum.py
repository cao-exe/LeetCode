class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            curr = nums[i]
            subtarget = target - curr
            for j in range(len(nums)):
                if nums[j] == subtarget and i != j:
                    indexes = [i,j]

        return indexes

        