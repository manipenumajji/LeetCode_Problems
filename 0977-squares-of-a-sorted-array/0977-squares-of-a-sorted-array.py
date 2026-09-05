class Solution:
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        for i in nums:
            return sorted(nums)
nums=[-4,-1,0,3,10]
s=Solution()
res=s.sortedSquares(nums)  
print(res)          
        