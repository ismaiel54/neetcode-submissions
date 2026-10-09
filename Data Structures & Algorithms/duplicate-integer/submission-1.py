class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hash = {}

        for i in range(len(nums)):
            if nums[i] in hash:
                return True 
            else:
                hash[nums[i]] = 1 + hash.get(nums[i], 0)

        return False
                