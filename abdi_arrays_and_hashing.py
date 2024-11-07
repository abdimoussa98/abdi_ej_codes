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