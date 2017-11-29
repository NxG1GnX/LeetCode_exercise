class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 题意：找出一个只含0、1的字符串中，0和1数目相等的子串，而且0和1要分组存在不可交叉
        # 分析：由于要求0和1分组存在，问题简化了很多，试想：当0和1各有一个，只有01、10两种情况，这时候只有一个符合要求的子串；
        #       当0和1各有两个，即0011或1100，这时符合要求的是2个子串……
        #       实际上我们把0和1分组计数（每变化一次就重新开始计数），每相邻的两个组之间，取min（），就是当前符合要求的子串数目
        #       再依次取min后相加即可
        ans = 0
        g = [1]
        
        for i in range(1,len(s)):
            if s[i-1] != s[i] :
                g.append(1)
            else:
                g[-1] += 1
        
        for j in range(1,len(g)):
            ans += min(g[j-1],g[j])
        
        return ans        
