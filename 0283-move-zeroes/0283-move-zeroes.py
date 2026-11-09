class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert = 0
        for i in nums:
            if i != 0:
                nums[insert] = i
                insert+= 1
        while(insert < len(nums)):
            nums[insert] = 0
            insert+=1
            
                
        return nums

        