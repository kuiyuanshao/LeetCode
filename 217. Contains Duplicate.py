class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use set() to get the distinct elements
        if len(nums) > len(set(nums)):
            return True
        else:
            return False
