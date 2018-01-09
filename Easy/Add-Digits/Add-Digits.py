class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num if num == 0 else num % 9 or 9
            
        
