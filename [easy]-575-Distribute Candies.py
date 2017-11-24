class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        kind = len(set(candies))
        num = len(candies)
        if kind<(num/2):
            return kind
        else:
            return num//2
        
