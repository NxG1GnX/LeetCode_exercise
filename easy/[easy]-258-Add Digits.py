class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        
        # reference：https://en.wikipedia.org/wiki/Digital_root
        # n的数根(digits root)即n除以9的余数，边缘情况是0、9的倍数
        
        return num%9 if num%9 != 0 or num==0 else 9
