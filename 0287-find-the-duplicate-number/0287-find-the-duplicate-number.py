class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # brute force method, two loops, o(n^2)

        # optimized method -> use hash set

        seen = set()

        for value in nums:
            if value in seen:
                return value
            seen.add(value)

        return -1
            
