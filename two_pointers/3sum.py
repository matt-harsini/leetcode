from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort the nums so it would be easier to track duplicate numbers adjacent to each other
        nums.sort()
        
        for i, a in enumerate(nums):
            # skip duplicates for a
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
           # same two some sorted logic 
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # we do this to skip duplicates again, we could have same a and same l pointer
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
   
app = Solution()
app.threeSum([-1, 0, 1, 2, -1, -4])                 