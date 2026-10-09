class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = {}
        res = []
        freq = [[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            count_map[nums[i]] = 1 + count_map.get(nums[i], 0)

        
        for n, c in count_map.items():
            freq[c].append(n)

        for i in range(len(freq) -1 , 0, -1):
            for b in freq[i]:
                res.append(b)
                if len(res) == k:
                    return res
            


        
            

