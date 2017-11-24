class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        
        L = []
        for op in ops:
            if op == 'C' :
                L.pop()
            elif op == 'D' :
                L.append(L[-1]*2)
            elif op == '+' :
                L.append(L[-1]+L[-2])
            else:
                L.append(int(op))
        
        return sum(L)       
        
        
