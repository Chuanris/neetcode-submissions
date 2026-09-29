class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for ik in nums:
            if ik in seen:
                return True
            seen.add(ik)
        return False