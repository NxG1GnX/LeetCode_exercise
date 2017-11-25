class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 一次最多拿3个，当轮到对手的时候只要场上还有4个，那最开始先拿的人就赢定了。
        # 于是策略为：我先拿，只要石头数量是4的倍数，只要第一次拿走余数，剩下的回合每次和对手拿互补的数就一定能赢
        # 一行代码即可
        
        return n%4 != 0
