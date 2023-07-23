# neetcodes solution

class neetcodes_solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
# my solution

class my_solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 0
            map[num] += 1
            if map[num] > 1:
                return True
        return False