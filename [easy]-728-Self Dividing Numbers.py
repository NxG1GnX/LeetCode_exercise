class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # (brute force)
        # 题目分析：1.判断range内的每一个数字，可以使用python的fliter特性简化循环
        #            即只返回符合要求的元素，这里的“要求”用boolean value来表示；
        #          2. 将int转换为str ----> set数据类型不含重复元素，可用来去重 
        #             -----> 0不能作为除数 ----> 用列表生成器得到每一次取余的结果
        #             -----> 全为0代表是self dividing number，返回true
 
        def check(num):
            digits = set(map(int, str(num)))
            if 0 in digits:return False
            return not any(num%i for i in digits)  # 列表生成器 
        ans = list(filter(check,range(left,right+1)))   # iterator 惰性序列 
        return ans 
