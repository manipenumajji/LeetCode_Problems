class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]

x = Solution()
print(x.twoSum([2, 7, 11, 15], 9))
print(x.twoSum([3, 2, 4], 6))        
print(x.twoSum([3, 3], 6))            
               
       
        