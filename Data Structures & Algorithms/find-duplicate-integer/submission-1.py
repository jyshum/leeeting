class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow] # next position is the value of each index
            fast = nums[nums[fast]] # next position is the next value of the next value of each index
            if slow == fast: 
                # if they equal each other, loop is confirmed in the index:
                # EX: since fast should always be ahead of slow , if slow somehow comes back to fast, it must mean  fast's loop comebacks to another step behind slow. Like in a linked list, the supposed end node should .next be None but it returns back to a node in the list. same idea here, since every value in the index is within the length of n, each value of each index should point to another index that has the same value as their index
                break

        slow2 = 0
        while slow != slow2:
            # while they dont equal to eachother, so both indexes can meet
            slow = nums[slow] # continue the loop of slow 
            slow2 = nums[slow2] # follow the same path as slow2

        return slow
        
