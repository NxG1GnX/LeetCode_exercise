class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 思路1：比较容易想到的
        #        bin()将一个int转化为str形式的二进制数，利用切片特性去掉前缀“0b”
        #        然后依次比较交替位是否一致，注意索引范围 
        
        b=bin(n)[2:]
        return all( b[i]!=b[i+1] for i in range(len(b)-1) ) 
        
        # 思路2：位运算
        #        一个整数n转化为二进制以后，右移两位（记为m1），将m1和n异或得到只有首位是1的数m2
        #        （m2-1）是一个首位0后面全1的数，计为m3，m3&m2==0
        return (n>>2)^n & ((n>>2)^n)-1 == 0
