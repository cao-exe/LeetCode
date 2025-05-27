class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            curr = nums[i]
            diff = target - curr
            if diff in seen:
                return [i, seen[diff]]
            else: 
                seen[curr] = i 

        