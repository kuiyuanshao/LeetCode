class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Use a dictionary to store the keys and elements
        uni_dict = {}
        for i in range(0, len(nums)):
            if nums[i] in uni_dict:
                if i - uni_dict[nums[i]] <= k:
                    return True
            uni_dict[nums[i]] = i
        return False
