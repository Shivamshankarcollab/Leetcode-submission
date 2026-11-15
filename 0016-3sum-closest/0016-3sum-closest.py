class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0]+nums[1] + nums[2]
        min = abs(closest_sum - target) 
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                total = nums[i] + nums[left]+nums[right]
                difference = abs(total - target)

                if difference < min:
                    min = difference
                    closest_sum = total
                if total < target:
                    left +=1
                elif total > target:
                    right -= 1
                else:
                    return total

        return closest_sum
            
            
            
        