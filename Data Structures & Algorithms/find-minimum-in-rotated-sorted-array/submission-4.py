class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minN = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                minN = min(nums[l], minN)
                break
            m = (l + r) // 2
            minN = min(nums[m], minN)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return minN