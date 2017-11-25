class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # 这题是个脑筋急转弯，理解题意是关键：当两个序列相等，就不存在Longest Uncommon Subsequence
        #                                  当两个序列不相等，最长的本身就是 Longest Uncommon Subsequence
        
        if a==b : return -1
        else : return max(len(a),len(b))        
