class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_count = 1
        dec_count = 1
        max_inc = 1
        max_dec = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                inc_count+=1
                if inc_count > max_inc:
                    max_inc = inc_count
            else:
                inc_count = 1
                

            if nums[i] > nums[i+1]:
                dec_count+=1
                if dec_count > max_dec:
                    max_dec = dec_count
            else:
                dec_count = 1
        
        return max(max_inc,max_dec)
            
        