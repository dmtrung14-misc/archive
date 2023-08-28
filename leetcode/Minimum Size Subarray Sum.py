leetcode/Minimum Size Subarray Sum.pyclass Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        res = len(nums)
        total = nums[0]
        pt1= pt2 = 0
        while pt2 < len(nums):
            if total < target:
                pt2 += 1
                total += nums[pt2] if pt2 != len(nums) else 0
            if total >= target:
                res = min(res, pt2 - pt1 + 1)
                
                total -= nums[pt1]
                pt1 += 1

        return res