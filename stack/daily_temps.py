from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = (i - stackIdx)
            stack.append([temperature, i])
        return res


app = Solution()

app.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
