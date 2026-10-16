class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i, n in enumerate(nums):
            result = target - n

            if result in count:
                return [count[result], i]
            
            count[n] = i
        return