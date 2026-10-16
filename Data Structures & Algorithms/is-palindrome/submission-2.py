class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 # first element
        right = len(s)-1 # last element

        while left < right: # we dont have to check the middle since theres nothing to compare it against
            while left < right and not s[left].isalnum():
                left += 1 # keep moving left until it finds a letter
            while left < right and not s[right].isalnum():
                right -= 1 # keep moving right

            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
        return True
            

        