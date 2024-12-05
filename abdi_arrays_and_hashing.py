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

# https://leetcode.com/problems/valid-anagram/description/
def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    freq_s = [0] * 26
    freq_t = [0] * 26

    for c in s: # o(n)
        freq_s[ord(c) - ord('a')] += 1
    for c in t: # o(n)
        freq_t[ord(c) - ord('a')] += 1

    print(freq_s)
    print(freq_t)

    if freq_s == freq_t:
        return True
    return False

# https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 2: return (0,1)

        prevMap = {}  # val -> index 

        for i, n in enumerate(nums): 
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

# https://leetcode.com/problems/group-anagrams/
    # BRUTE FORCE
    # result = []

    # ["eat"] : ["eat","tea","tan","ate","nat","bat"] = [eat, ate, tea]
    # copy ["tan","nat","bat"]
    # result.append([eat, ate, tea])

    # ["tan"] : ["tan","nat","bat"] = ["tan","nat"]
    # copy ["bat"]
    # result.append(["tan","nat"])

    # ["bat"] : ["bat"] = [bat]
    # copy []
    # result.append([bat])

    # return result

import collections
def dfs(self, strs, result):
    if len(strs) == 0: return

    not_matching = []
    matching = []

    for s in strs:
        if (collections.Counter(strs[0]) == collections.Counter(s)):
            matching.append(s)
        else:
            not_matching.append(s)
            
    result.append(matching)
    self.dfs(not_matching, result)

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    result = []
    self.dfs(strs, result)
    return result

# https://leetcode.com/problems/top-k-frequent-elements/

def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        frequency_map = collections.Counter(nums)
        sorted_map = sorted(frequency_map.items(), key=lambda item: item[1], reverse=True)
        for idx in range(k):
            result.append(sorted_map[idx][0])
        return result

def bucketSortTopKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        bucket_sort_list = [[] for i in range(len(nums) + 1)]
        frequency_map = collections.Counter(nums)
        result = []

        for item in frequency_map.items():
             bucket_sort_list[item[1]].append(item[0])
        
        for idx in range(len(bucket_sort_list)-1, 0, -1):
            for x in bucket_sort_list[idx]:
                if k > 0: 
                        result.append(x)
                        k -= 1
                else: return result
        return result
                  
        # for i in range(len(freq) - 1, 0, -1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k: MUCH CLEANER!!!!
        #             return res

# https://leetcode.com/problems/product-of-array-except-self/
# with division
def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    num_zeros = 0
    prod = 1
    
    for num in nums:
        if num == 0:
                num_zeros += 1
        else: 
            prod = prod * num
    
    if num_zeros > 1:
        for idx in range(len(nums)):
            nums[idx] = 0
        return nums

    for idx, num in enumerate(nums):
        if num != 0 and num_zeros != 1:
                nums[idx] = prod // num
        elif num == 0: 
            nums[idx] = prod
        else: 
            nums[idx] = 0
    
    return nums

# with fromLeftRunningProduct and fromRightRunningProduct (Prefix & Suffix (Optimal))
def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # result = [0 for i in range(len(nums))]
    result = [0] * (len(nums))

    leftProd = 1
    for idx in range(len(nums)):
        result[idx] = leftProd
        leftProd *= nums[idx]
    
    rightProd = 1
    for idx in range(len(nums) - 1, -1, -1):
        result[idx] *= rightProd
        rightProd *= nums[idx] 
    return result

# https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            prev = set()
            for el in row:
                if el != '.':
                    if el in prev:
                        return False
                    else:
                        prev.add(el)

        for c in range(9): # first loop will always increment after the completion of the second loop
            prev = set()
            for r in range(9):
                if board[r][c] != '.':
                    if board[r][c] in prev:
                        return False
                    else:
                        prev.add(board[r][c])

        for y_inc in range(0, 9, 3):
            for x_inc in range(0, 9, 3):
                if not self.subBox((0+x_inc, 3+x_inc), (0+y_inc, 3+y_inc), board):
                    return False

        return True
    
    def subBox(self, x_points, y_points, board):
        prev = set()
        for c in range(y_points[0],y_points[1]):
            for r in range(x_points[0],x_points[1]):
                if board[c][r] != '.':
                    if board[c][r] in prev:
                        return False
                    else:
                        prev.add(board[c][r])
        return True
            
    # x(0-2)    x(3-5)      x(6-8)
    # y(0-2)    y(0-2)      y(0-2)
    # [000]     [000]       [000]
    # [000]     [000]       [000]
    # [000]     [000]       [000]

    # x(0-2)    x(3-5)      x(6-8)
    # y(3-5)    y(3-5)      y(3-5)
    # [000]     [000]       [000]
    # [000]     [000]       [000]
    # [000]     [000]       [000]

    # x(0-2)    x(3-5)      x(6-8)
    # y(6-8)    y(6-8)      y(6-8)
    # [000]     [000]       [000]
    # [000]     [000]       [000]
    # [000]     [000]       [000]

