# https://leetcode.com/problems/contains-duplicate/description/


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      
         for currEl in nums: 
            nextEl = currEl + 1

            for nextEl in nums: 
                # if nums.index(nextEl) == len(nums)-1: break
                if currEl == nextEl:
                    return True
                nextEl = nextEl + 1
            
            currEl = currEl + 1