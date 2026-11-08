class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        
        temp = x
        while(temp > 0 ):
            digit = temp % 10
            rev = (rev * 10) + digit
            temp = temp // 10
        

        if x == rev:
            return True
        else:
            return False
        