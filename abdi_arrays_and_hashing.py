# https://leetcode.com/problems/contains-duplicate/description/


def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        check = set()
        for num in nums:
            if num in check:
                return True
            else: 
                check.add(num)
    
        return False
