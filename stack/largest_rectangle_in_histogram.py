from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> List[int]:

        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            # if the current height we are iterating on is greater than the rect height
            # at the top of our stack, we skip the while loop, this is monotonic stack increasing order
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            # once the while loop condition is no longer true, we append the start index and
            # current height we are iterating on. the start index would be the last element we popped + current height
            stack.append((start, h))
        # this works because the stack would be in monotonic increasing order in regards to the height
        # so we just take the length of height and subtract the respective index associated with the height
        # because the rectangle can extend all the way to the right
        for i, h in stack:
            currArea = h * (len(heights) - i)
            maxArea = max(maxArea, currArea)
        return maxArea


app = Solution()

app.largestRectangleArea([2, 1, 5, 6, 2, 3])
