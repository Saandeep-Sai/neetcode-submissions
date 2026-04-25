class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        print(setNums)
        longest = 0
        for n in nums:
            length = 0
            while (n+length) in nums:
                length += 1
            longest = max(length,longest)
        return longest