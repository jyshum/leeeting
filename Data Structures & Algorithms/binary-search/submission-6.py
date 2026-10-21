class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # brute force w/ o(n) -> iterate through every element in the list 

        for i, value in enumerate(nums):
            if value == target:
                return i
        
        return -1

