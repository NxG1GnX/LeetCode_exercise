class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = ans = 0
        for i in nums:
            if i==1 :
                a += 1
                ans = max(a,ans)
            else: 
                a = 0
        return ans
