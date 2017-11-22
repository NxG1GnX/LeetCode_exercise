class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # 汉明距离：两个相同长度字对应位不同的数量
        # 非常简单：异或，然后统计1的数目即可
        z = str(bin(x^y))
        return z.count('1')
