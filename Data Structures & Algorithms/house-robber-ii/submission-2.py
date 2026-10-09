class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        

    def helper(self, nums):
        nu = len(nums)
        prev, curr = nums[0], max(nums[0], nums[1])
        for i in range(2, nu):
            tmp = max(nums[i] + prev, curr)
            prev = curr
            curr = tmp
            
        return curr



