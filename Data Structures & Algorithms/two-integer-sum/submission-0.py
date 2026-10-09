class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            n = target - nums[i]
            if n in hash:
                return [hash[n], i]
            else:
                hash[nums[i]] = i