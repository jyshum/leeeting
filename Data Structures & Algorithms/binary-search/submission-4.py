class Solution:
    def search(self, nums: List[int], target: int) -> int:
        top = len(nums)-1
        bottom = 0

        while top >= bottom:
            middle = (top+bottom)//2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                top = middle - 1
            elif target > nums[middle]:
                bottom = middle + 1

        return -1