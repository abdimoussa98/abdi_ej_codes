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