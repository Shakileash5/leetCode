
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Problem Description

# Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alphaStore = set()
        start = 0
        end = 0
        n = len(s)
        maxSubString = 1
        if s == "":
            return 0
        while end<n:
            if s[end] in alphaStore:
                alphaStore.remove(s[start])
                start +=1         
            else:
                alphaStore.add(s[end])
                maxSubString = max(end - start +1 ,maxSubString)
                end+=1   
        return maxSubString