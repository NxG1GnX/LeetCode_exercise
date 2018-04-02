class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num = 0
        jewel = set(J)
        for i in S:
            if i in jewel : num = num + 1
        return num
        
