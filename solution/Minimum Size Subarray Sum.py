class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float('inf')
        l,sum =0,0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                minlen = min(minlen, r-l+1)
                sum -= nums[l]
                l += 1
        return minlen if minlen<=len(nums) else 0