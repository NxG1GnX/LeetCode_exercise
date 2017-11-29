class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
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
