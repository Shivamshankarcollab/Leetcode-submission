class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        blue = 0
        white = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                red +=1
            elif nums[i] == 1:
                white+=1
            elif nums[i] == 2:
                blue +=1
        for  j in range(red):
            nums[j] = 0
        white = white + red
        for j in range(red,white):
            nums[j] = 1
        blue = white + blue
        for j in range(white,blue):
            nums[j] = 2
        

        


        