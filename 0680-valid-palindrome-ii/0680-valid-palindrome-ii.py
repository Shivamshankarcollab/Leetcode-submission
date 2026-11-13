class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                temp = s[left+1:right+1]
                if temp == temp[::-1]:
                    return True
                temp = s[left:right]
                if temp == temp[::-1]:
                    return True
                return False
            left +=1
            right -=1
            
        return True
            

        