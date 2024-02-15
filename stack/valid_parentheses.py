class Solution:
    def isValid(self, s: str) -> bool:

        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                # we know that if c is not in Map, it's a opening bracket. The "in" checks if the key is in a dict or not
                # not the value
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack

app = Solution()
app.isValid(")))))")