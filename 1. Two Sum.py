import numpy as np
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Get the subtraction of target to nums list
        rev = np.subtract([target] * len(nums), nums)
        #An empty list
        loc = []
        for i in nums:
            # element i won't equal to the target number
            # if element i within the rev get into the if
            if np.count_nonzero(rev == i) == 1 and target - i != i:
                #Get the index of i
                ind = np.where(rev == i)[0]
                loc.append(int(ind))
            # if there two elements are the same (a special case)
            elif np.count_nonzero(rev == i) == 2:
                ind = np.where(rev == i)[0].tolist()
                loc.append(ind)
        loc.reverse()

        if isinstance(loc[0], list):
            return(loc[0])
        else:
            return(loc)
