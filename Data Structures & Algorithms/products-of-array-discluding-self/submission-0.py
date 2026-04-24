class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output =[]
        pref_res=1
        suf_res=1
        for i in range(len(nums)):
            #prefix result
            for j in nums[i+1:len(nums)]:
                pref_res *= j
            for j in nums[0:i]:
                suf_res *= j
            output.append(pref_res*suf_res)
            pref_res =1
            suf_res = 1
        return output