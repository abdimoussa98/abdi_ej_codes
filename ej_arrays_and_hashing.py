# https://leetcode.com/problems/contains-duplicate/description/
def hasDuplicate(self, nums: List[int]) -> bool:

    for currEl in nums: 
        nextEl = currEl + 1

    for nextEl in nums: 
        # if nums.index(nextEl) == len(nums)-1: break
        if currEl == nextEl:
            return True
        nextEl = nextEl + 1
    
    currEl = currEl + 1

# https://leetcode.com/problems/valid-anagram/description/
def isAnagram(self, s: str, t: str) -> bool:
    sortedS = sorted(s) #n log n
    sortedT = sorted(t) # n log n
    
    return sortedS == sortedT #o(n)
    # if len(sortedS) == len(sortedT)
    #     for i in range(len(sortedS)):
    #         if sortedS[i] != sortedT[i]:
    #             return False
    #     return True
    
    # return False