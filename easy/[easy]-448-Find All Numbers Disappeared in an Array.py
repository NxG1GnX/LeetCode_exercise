class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 正负号标记法，将元素和索引联系起来
        # python中enumerate（）的用法
        
        for i in nums:
            nums[abs(i)-1] = -abs(nums[abs(i)-1])
        
        return [i+1 for i,j in enumerate(nums) if j>0]
