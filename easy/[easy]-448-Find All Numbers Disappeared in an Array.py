class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
            nums[abs(i)-1] = -abs(nums[abs(i)-1])
        
        return [i+1 for i,j in enumerate(nums) if j>0]
