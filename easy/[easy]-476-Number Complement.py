class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        i = 1
        while i <= num:
            num=num^i
            i<<=1
        return num
