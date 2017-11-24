class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def trans(i):
            if i%15==0 : return 'FizzBuzz'
            elif i%3==0 : return 'Fizz'
            elif i%5==0 : return 'Buzz'
            else : return str(i)
       
        return list(map(trans,range(1,n+1)))
