class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 方法1： 先把不为0的数全部移到前面，再把后边的数依次置为0，需要用到一个变量表示“”指针
        i = 0
        for n in nums:
            if n != 0 :
                nums[i] = n
                i += 1
        for j in range(i,len(nums)):
            nums[j]=0
            
        # 方法2 ：虽然AC了但是觉得有问题，暂时存在这里
        # index返回的其实还是第一个位置的0
        # 这个代码只是碰巧通过了
        # 后患无穷
        
        for i in nums:
            if i==0:
                nums.pop(nums.index(i))
                nums.append(0)
