from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            # if the top of the stack (which represents the speed of the car) is faster (which means less then stack[-2]), then
            # you have car fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

app = Solution()

app.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])