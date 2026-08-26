class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quick_Select(l,r):
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = pivot, nums[p]

            if p > k:
                return quick_Select(l,p-1)
            elif p < k:
                return quick_Select(p+1,r)
            else:
                return nums[p]
        return quick_Select(0, len(nums)-1)