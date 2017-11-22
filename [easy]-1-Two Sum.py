class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            x = target - nums[i]
            if x in nums and nums.index(x)!=i:                
                return (nums.index(x),i) if nums.index(x)<i else (i,nums.index(x))
