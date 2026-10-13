class Solution:
    def isAnagram(self, s, t):
        # cheese method -> sort both strings and see if they == 

        # o(n) time
        # create hashmaps of each string representing their frequency of letters
        # then compare
        
        sStr = {}
        for char in s:
            if char in sStr:
                sStr[char] += 1
            else:
                sStr[char] = 1
        tStr = {}
        for char in t:
            if char in tStr:
                tStr[char] += 1
            else:
                tStr[char] = 1
        
        if sStr == tStr:
            return True
        else:
            return False


        
        

        


        

        

        

    
            



                    

