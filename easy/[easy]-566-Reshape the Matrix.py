class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        L = []
        num = sum(nums,[])
        if r*c != len(num):return nums
        else:
            [m,n] = [0,c]
            for i in range(r):
                L.append(num[m:n])
                m,n = m + c,n + c
            return L
