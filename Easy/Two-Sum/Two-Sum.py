class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for counter, num in enumerate(nums):
            new=target-num
            if new in d:#if no is in dictionary
                return [d.get(new),counter]#then return counter and key value of the no
            else:
                d[num]=counter#if no match then add to dict with key and value

            
            
        
        