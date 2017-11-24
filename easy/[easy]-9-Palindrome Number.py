class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 原题hints：1.这个问题有通用解法； 2.不用字符串;  3.需要考虑生成反转数字时的溢出问题；
        # 思路：
        #       1. 每次比较头尾两个数，不相等返回false，相等则掐头去尾继续比较；
        #       2. 生成反转数字，pathon因为语言特性不需要考虑数据类型导致的溢出，但不是最优；
        #       3. 2的改进，只生成一半的反转数字。
        
        if x<0 :
            return False
        else:
            d = 1
            while x/d >= 10 :
                d *= 10
            
            while d>1 :
                l = x%10  # 取尾
                r = x//d  # 取头
                if l != r:return False
                x = (x%d)//10 #掐头去尾
                d = d/100
            return True
