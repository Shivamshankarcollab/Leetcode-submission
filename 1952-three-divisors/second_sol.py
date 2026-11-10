import math
class Solution:
    def isThree(self, n: int) -> bool:
        root = math.isqrt(n)

        if root * root == n:
            if root < 2 :
                return False
            for i in range(2,int(root ** 0.5)+1):
                if root % i == 0:
                    return False
        if root * root != n:
            return False
        return True
                    

        
            
            
        
            
        
