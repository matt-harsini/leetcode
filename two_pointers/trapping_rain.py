from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            # we add to result if leftMax is less than rightMax since leftMax is the bottleneck
            # we cannot add more water than leftMax can hold, or else it will spill to the left
            if leftMax < rightMax:
                l += 1
                # next two line computations:
                # leftMax will never be negative because only two optiosn can occur
                # leftMax is the max and we subtract height[l] which will be positive
                # height[l] is the max and we subtract it by itsself in the res += leftMax - height[l]
                # same logic in the else statement
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            # vice versa for rightMax, we cannot add more water than rightMax capacity
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


app = Solution()
app.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])