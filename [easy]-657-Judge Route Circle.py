class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # 方法1：为了练习map/reduce/filter等特性，此方法很慢，解决该问题有很简单的思路
        
        from functools import reduce
        import numpy as np
        
        def go(x,y):            
            return np.add(x,y)
        d = {'U':[0,1],'D':[0,-1],'L':[-1,0],'R':[1,0]}
        m = reduce(go,[d[moves[step]] for step in range(len(moves))])
        if m[0]==m[1]==0:return True
        else:return False
        
        #方法2： 直接比较moves中U与D、L和R的数目是否相等即可
        if moves.count('U')==moves.count('D') and moves.count('L')==moves.count('R'):return True
        else:return False
