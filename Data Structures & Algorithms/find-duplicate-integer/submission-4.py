class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        # find if slow and fast meetup again
        while True: # a true loop never breaks on its own, something has to break it out
            # keep iterating slow and fast until they meet -> we found it
            slow = nums[slow] # 1 step
            fast = nums[nums[fast]] # 2 step
            if slow == fast: # condition to break the loop
                break

        slow2 = 0 
        while slow != slow2: # find the dup by resertting one pointer and see where they meet
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow2