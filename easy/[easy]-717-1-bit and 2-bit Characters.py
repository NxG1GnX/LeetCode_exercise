class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        # 字符编码，由于只能存在0、10、11这三种情况，当最后一个digits是1时，必然不是one-bit character
        # 从首位开始检查，当为1时，随后的数字是0或1都行，所以跳过下一位；当为0时，以0开头的只有一种情况，继续检查。
        
        if bits[-1]==1 :return False
        else:
            i = 0
            while i<len(bits):
                if i == len(bits)-1:return True
                elif bits[i]==0:i+=1
                else:i+=2  
            return False
