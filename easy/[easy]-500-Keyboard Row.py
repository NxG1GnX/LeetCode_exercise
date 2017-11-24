class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def check(w):
            row1 = "qwertyuiop"
            row2 = "asdfghjkl"
            row3 = "zxcvbnm"
            w = str.lower(w)  
            if (set(w)&set(row1) == set(w)) or (set(w)&set(row2) == set(w)) or (set(w)&set(row3) == set(w)):
                return True
   
        return list(filter(check,words))
