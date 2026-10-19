class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # create a hashmap of each string in strs in [letter, index]
        # if they match, then we can add the prefix

        prefix = "" # keep track of prefix so far
        for i in range(len(strs[0])): # iterating through each character placement of string #0 in strs
            for string in strs: # iterate through every string in strs
                if i == len(string) or string[i] != strs[0][i]: 
                    # check for out of bounds(if the pointer is not in the length of the string we're checking)
                    # comparing "batt" & "ba" -> pointer is at 2 checking t in batt, but theres no third letter in ba
                    # automantically return the prefix which should be ba
                    return prefix
            prefix += strs[0][i] # compare to first string

        return prefix