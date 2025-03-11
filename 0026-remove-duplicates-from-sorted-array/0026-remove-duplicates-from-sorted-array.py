class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        k = 1
        curr = nums[0]
        for i in range(len(nums)):
            val = nums[i]
            if val != curr:
                nums[k] = val
                k += 1
                curr = val

        return k 
        
            
        
        