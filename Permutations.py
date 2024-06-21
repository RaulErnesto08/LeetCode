from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return [[]]

        result = []
        
        for i in range(len(nums)):
            current = nums[i]
            remaining = nums[:i] + nums[i+1:]
        
            for permutation in self.permute(remaining):
                result.append([current] + permutation)
        
        return result
