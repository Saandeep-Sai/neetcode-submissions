class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = max(nums)
        n = min(nums)

        if target > k or target < n:
            return -1
        
        l = 0
        r = len(nums)-1

        x = []
        y = []
        
        while l<=r:
            mid = (l+r)//2
    
            if nums[mid] < 0:
                r = mid-1
                continue
            if nums[l] == k:
                x = nums[0:l+1]
                y = nums[l+1:len(nums)]
            if nums[r] == k:
                x = nums[0:r+1]
                y = []
            if nums[mid] == k:
                x = nums[0:mid+1]
        
                y = nums[mid+1:len(nums)]
        
                break
            else:
                l = mid+1

        #searching target in x
        if len(x) != 0:
            if x[0] <= target:
                l = 0
                r = len(x)-1
                while l<=r:
                    mid = (l+r)//2
                    if x[mid] == target:
                        return mid
                    elif x[mid] < target:
                        l = mid+1
                    else:
                        r = mid-1
        if len(y) != 0:
            if y[len(y)-1] >= target:
                l = 0
                r = len(y)-1
                while l<=r:
                    mid = (l+r)//2
                    if y[mid] == target:
                        return len(x)+mid
                    elif y[mid] < target:
                        l = mid+1
                    else:
                        r = mid-1
        return -1