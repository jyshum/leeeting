class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set() # create set to keep track of elements in window
        l = 0 # set left pointer at the start 
        best = 0 # keep track of substring lengths
        for r in range(len(s)): # from 0 to last element
            while s[r] in seen: 
                # keeps removing elements until there is no more duplicate of s[r]
                seen.remove(s[l]) # removes left
                l += 1 # shifts pointer
            
            seen.add(s[r])
            best = max(best, r-l+1)

        return best