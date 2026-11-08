class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        even_count =0 
        
        for i in nums:
            count = 0
            while ( i > 0 ):
                i % 10
                count=count+1
                i = i // 10
            if count % 2 == 0:
                even_count=even_count+1
        return even_count

            
        