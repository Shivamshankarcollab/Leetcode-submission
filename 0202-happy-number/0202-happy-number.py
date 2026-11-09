class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        while ( n != 1 ):
            if n in seen:
                return False
            seen.add(n)
            temp = n
            sum = 0 
            while temp > 0:
                digit = temp % 10 
                sum += digit * digit
                temp = temp // 10
            n = sum
            
        if n == 1:
            return True
            
            

    

        