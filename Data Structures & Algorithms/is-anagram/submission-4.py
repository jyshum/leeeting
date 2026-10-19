class Solution:
    def isAnagram(self, s, t):
        # brute force method -> sort both strings and compare -> o(n) time comp becuz create new lists
        # optimized method -> hashmaps -> iterating through s and t once

        seenS = {} # [letter, frequency]
        for char in s:
            if char in seenS:
                seenS[char] += 1 # add freq
            else:
                seenS[char] = 1 # enlist new char
        
        seenT = {}
        for char in t:
            if char in seenT:
                seenT[char] += 1
            else:
                seenT[char] = 1

        # compare
        if seenT == seenS:
            return True
        else:
            return False
        

        
        

        


        

        

        

    
            



                    

