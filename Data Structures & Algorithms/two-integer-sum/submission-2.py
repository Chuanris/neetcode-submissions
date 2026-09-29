class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, k in enumerate(nums):
            for j, l in enumerate(nums):
                if i != j and k + l == target:
                    return [i,j]