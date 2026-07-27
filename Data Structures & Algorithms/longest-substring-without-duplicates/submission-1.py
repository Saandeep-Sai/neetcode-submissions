class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,1
        longest_substring = 0

        if len(s) == 1:
            longest_substring = 1
        while r < len(s):
            if s[r] not in s[l:r]:
                longest_substring = max(longest_substring,r-l+1)
                r += 1
            else:
                l += 1
                
        return longest_substring