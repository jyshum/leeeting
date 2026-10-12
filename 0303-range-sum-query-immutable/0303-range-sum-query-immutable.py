class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        
    def sumRange(self, left: int, right: int) -> int:
        outputSum = 0

        while left <= right:
            outputSum += self.nums[left]
            left += 1

        return outputSum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)