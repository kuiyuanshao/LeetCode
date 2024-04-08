class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        n = len(nums1)
        check = n % 2
        if check == 0:
            ind1 = int(n / 2 - 1)
            return sum(nums1[ind1:(ind1 + 2)]) / 2
        else:
            return (nums1[int(n / 2)])
