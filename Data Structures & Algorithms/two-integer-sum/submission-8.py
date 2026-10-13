class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # outputting indices 
        # taking in values[i & j] and seeing if they add up to target

        # O(n^2)
        # for i in range(len(nums)):
            # for j in range(i+1, len(nums)):
                # if nums[i] + nums[j] == target:
                    # return [i, j]

        # O(n)
        hashMap = {}
        for i, number in enumerate(nums):
            value = target - number # every loop, re-initialize what the value is, this way you can figure out if there is another value in the array that matches the value at the current index the loop is on, and so forth
            if value in hashMap:
                return [hashMap[value], i] 
            hashMap[number] = i # we're setting the key of the hashMap to the values in the array, not the indices; since we're using hashmaps and we're trying to look for the "value", the key in the hashMap is the value. Here we're just making it so we're creating a dict of keys and values so we can keep track of all key and values by storing it here as we keep going through the array
            
